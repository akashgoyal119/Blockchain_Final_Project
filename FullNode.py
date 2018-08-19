from __future__ import print_function
from concurrent import futures
import grpc, socket, time, random, threading
import json, pickle

import registrar_pb2
import registrar_pb2_grpc
import full_node_pb2
import full_node_pb2_grpc

from MagicCoin.MC_Block import Block
from MagicCoin.MC_BlockChain import BlockChain
from MagicCoin.MC_Miner import Miner
from MagicCoin.MC_Output import Output
from MagicCoin.MC_Transaction import Transaction
from MagicCoin.MC_TxnMemoryPool import TxnMemoryPool
from MagicCoin.MC_Contract import Contract
from MagicCoin.MC_ContractMemoryPool import ContractMemoryPool
from MagicCoin.MC_User import User
import uuid


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class FullNode(full_node_pb2_grpc.FullNodeServicer):

	def __init__(self):
		self.known_peers_list = []	# list of known peers (return receiving handshake request)
		self.handshaken_peers_list = []	# keep track of nodes already shaken hands with
		genesis_block = Block.generate_genesis_block()
		self.blockchain = BlockChain(genesis_block)		# Initialize BlockChain with genesis_block
		self.txn_pool = TxnMemoryPool(number_of_txn=0)	# Initialize empty txn pool
		self.miner = Miner()	# Initialize miner
		public_key = str(uuid.uuid4())
		self.user = User(public_key=public_key)
		self.contract_pool = ContractMemoryPool(number_of_contract=0)
	
	def handshake(self, request, context):
		"""Receives handshake request from a newly joined node
		and returns ip addresses of all known nodes.
		If the handshake calling node is new to the receiving node, the
		receiving node will initiate handshake with that node.
		
		Note: This algorithm allows each node to shake hands with 
		all the other nodes in the network exactly once.
		"""
		print('\nHandshake RECEIVED from         : ' + request.addrMe)
		# only add new ip address
		if request.addrMe not in self.known_peers_list:
			self.known_peers_list.append(request.addrMe)
		print('Handshake RESPONSE (known nodes): ' + '  '.join(self.known_peers_list) +'\n')
		response = full_node_pb2.hs_reply()
		for ip_addr in self.known_peers_list:
			response.message.append(ip_addr)
		# initiate handshake with newly added peer.
		if request.addrMe not in self.handshaken_peers_list:
			self.request_handshake(request.addrMe)
		# if the new node's local blockchain is not complete,
		# send the blocks that the new node needs in order to
		# start mining.
		if request.bestHeight < self.blockchain.height():
			print('###########################################')
			print(f'Need to send Blocks to node: {request.addrMe}')
			for i in range(request.bestHeight+1, self.blockchain.height()+1):
				block_to_send = self.blockchain.get_block_by_height(i)
				self.send_block_to_node(
					block_to_send=block_to_send, 
					receiving_node=request.addrMe, 
					block_height=i)
			print('###########################################')
		return response

	def request_handshake(self, ip_addr):
		"""Requests handshake to ip_addr and
		returns list of known ip address from the
		handshake receiving node.
		"""
		self.handshaken_peers_list.append(ip_addr)
		print("\nRequesting handshake to node: " + ip_addr)
		with grpc.insecure_channel(ip_addr+':12345') as channel:
			stub = full_node_pb2_grpc.FullNodeStub(channel)
			# hs_response is a list of ip address
			hs_response = stub.handshake(
				full_node_pb2.hs_request(nVersion=1,
										nTime=current_time(),
										addrMe=get_ip(),
										bestHeight=self.blockchain.height())
			)
		print(f"Received list of known nodes: {'  '.join(hs_response.message)}")
		#print(f"Current Node's list of known nodes: {'  '.join(self.handshaken_peers_list)}\n")
		print(f"Current Node's list of known nodes: {'  '.join(self.known_peers_list)}\n")
		return hs_response.message

	def send_block_to_node(self, block_to_send, receiving_node, block_height):
		"""Sends blocks to the newly joined node if that node
		has incomplete blockchain.

		Note: This method is implemented with the purpose of
		avoiding forks.
		"""
		serialized_block = pickle.dumps(block_to_send)
		with grpc.insecure_channel(receiving_node+':12345') as channel:
			stub = full_node_pb2_grpc.FullNodeStub(channel)
			existing_block = full_node_pb2.Block(serialized_block=serialized_block)
			response = stub.existing_block_broadcast(existing_block)
		print(f"Sending BLOCK in BlockChain Height {block_height} to: {receiving_node}")
	
	def broadcast_block(self, new_block):
		"""Broadcasts newly mined block to other peers
		in the network.
		"""
		serialized_block = pickle.dumps(new_block)
		for ip_addr in self.known_peers_list:
			with grpc.insecure_channel(ip_addr+':12345') as channel:
				stub = full_node_pb2_grpc.FullNodeStub(channel)
				new_block = full_node_pb2.Block(serialized_block=serialized_block)
				response = stub.new_block_broadcast(new_block)
			print(f"Broadcasting New Block to: {ip_addr}")
		# after publishing a new block to other known peers, sleep between 0-3 seconds
		sleep_interval = random.uniform(2, 3)
		print(f"... After broadcasting new block to other nodes, sleep for: {sleep_interval} seconds ...")
		time.sleep(sleep_interval)

	def existing_block_broadcast(self, request, context):
		"""Receives blocks from other nodes and locally builds
		the node's blockchain.

		Note: This method ensures the consistency of the blockchain
		by receiving existing blocks to the newly joined node's blockchain
		so that newly joined nodes blockchain are the same length as the
		the network's best blockchain.
		"""
		# instantiate new Block() object using the new block's transaction list created above.
		new_block = pickle.loads(request.serialized_block)
		# add new block to local BlockChain() object.
		self.blockchain.add_block(new_block)
		print('**************************************')
		print('... EXISTING BLOCK RECEIVED ...')
		print('... EXISTING BLOCK ADDED TO BLOCKCHAIN ...')
		print(f'BLOCKCHAIN HEIGHT: {self.blockchain.height()}')
		print('**************************************')
		# remove already mined transactions from local txn_memory_pool
		self.remove_mined_transaction_from_memory_pool(mined_transactions=new_block.transactions)
		response = full_node_pb2.block_broadcast_reply(message="broadcast received")
		return response

	def new_block_broadcast(self, request, context):
		"""Receives new block broadcast.
		Deletes any transaction in the working transaction pool
		that is included in the new block.
		"""
		# instantiate new Block() object using the new block's transaction list created above.
		new_block = pickle.loads(request.serialized_block)
		# add new block to local BlockChain() object.
		self.blockchain.add_block(new_block)
		print('**************************************')
		print('... NEW BLOCK RECEIVED ...')
		print('... NEW BLOCK ADDED TO BLOCKCHAIN ...')
		print(f'BLOCKCHAIN HEIGHT: {self.blockchain.height()}')
		print('**************************************')
		# remove already mined transactions from local txn_memory_pool
		self.remove_mined_transaction_from_memory_pool(mined_transactions=new_block.transactions)
		# after a new block is published and added to the blockchain,
		# each miner sleeps between 0-3 seconds
		sleep_interval = random.uniform(2, 3)
		print(f"... After adding new block from other nodes, sleep for: {sleep_interval} seconds ...")
		time.sleep(sleep_interval)
		
		response = full_node_pb2.block_broadcast_reply(message="broadcast received")
		return response

	def remove_mined_transaction_from_memory_pool(self, mined_transactions):
		"""	Scan local valid transaction memory pool and if there is a 
		transaction that has already been included in the new block,
		remove that transaction from the local valid transaction memory pool.
		"""
		for txn_in_local_pool in self.txn_pool.valid_list:
			if txn_in_local_pool.transaction_hash in mined_transactions:
				self.txn_pool.valid_list.remove(txn_in_local_pool)
				print(f'Removing transaction from memory pool: {txn_in_local_pool.transaction_hash}')
		print('\n**************************************')
		print('Local transaction memory pool updated.')
		print('**************************************\n')

	def start_mining(self, working_memory_pool):
		"""Start mining a new block with the transactions
		in the working memory pool.
		"""
		# get previous block to get the block hash value
		previous_block = self.blockchain.get_most_recent_block()
		# mine new block
		# total_mining_fee includes coinbase_reward and the sum of all transaction fees
		new_block, total_mining_fee = self.miner.mine_new_block(
			previous_block, working_memory_pool
		)
		# Only add the newly mined block if the prev_block_hash value matches,
		# otherwise, start mining for a new block again.
		# The infinite while-loop in "mine_and_broadcast_new_block()" method
		# will automatically start mining a new block.
		if self.blockchain.get_most_recent_block().block_hash() == new_block.hash_prev_block_header:
			# add new block to blockchain of the node
			self.blockchain.add_block(new_block)
			# broadcast new block to other peers in the network
			self.broadcast_block(new_block)
			print('================================')
			print('... NEW BLOCK MINED ...')
			print('... ADDING NEW BLOCK TO BLOCKCHAIN ...')
			print('... BROADCASTING NEW BLOCK TO OTHER NODES ...')
			print(f'BLOCKCHAIN HEIGHT: {self.blockchain.height()}')
			print(f'MagicCoin Rewarded (Reward + Transaction Fees): {total_mining_fee} quidditch')
			print('================================')	

	def mine_and_broadcast_new_block(self):
		"""Constantly mines new blocks and broadcasts them
		to other nodes in the network.
		"""
		while True:
			# working memory pool for transactions to be included in the new block
			new_block_txn_list = []	
			if len(self.txn_pool.valid_list) <= 0:
				# if there are no transactions, do not mine for new block.
				continue
			elif len(self.txn_pool.valid_list) <= (Block.MAX_TXNS - 1):
				# if there are less number of txn left than MAX_TXNS
            	# create new block with the remaining txns.
				for i in range(len(self.txn_pool.valid_list)):
					txn = self.txn_pool.get_transaction()
					new_block_txn_list.append(txn)
				self.start_mining(working_memory_pool=new_block_txn_list)
			else:
				# create new block by consuming transactions from
            	# the txn_memory_pool
				for i in range(Block.MAX_TXNS - 1):
					txn = self.txn_pool.get_transaction()
					new_block_txn_list.append(txn)
				self.start_mining(working_memory_pool=new_block_txn_list)

	def generate_contract(self):
		"""Generate new contract object.
		"""
		contract = self.user.generate_random_contract()
		# add to memory pool
		self.contract_pool.add_contract(contract)
		print('++++++++++++++++++++++++++++++++++++++++++++')
		print('Generated contract:')
		print(f'{contract.contract_hash_value}')
		print(f'CONTRACT MEMORY POOL SIZE: {len(self.contract_pool.list)}')
		print('++++++++++++++++++++++++++++++++++++++++++++')
		return contract

	def new_contract_broadcast(self, request, context):
		broadcast_node = request.broadcast_node
		# instantiate Contract object
		contract = pickle.loads(request.serialized_contract)
		print(f'Received contract from: {broadcast_node}')
		need_to_broadcast = True
		# if the received contract already exists in the memory pool, do nothing
		try:
			for c in self.contract_pool.list:
				if contract.contract_hash_value == c.contract_hash_value:
					print(f'Contract already exists in memory pool: {contract.contract_hash_value}')
					need_to_broadcast = False
		except:
			pass
		response = full_node_pb2.contract_broadcast_reply(message="contract received")
		return response

	def broadcast_contract(self, contract, broadcast_node):
		serialized_contract = pickle.dumps(contract)
		for ip_addr in self.known_peers_list:
			if ip_addr != broadcast_node:
				print(f'Broadcasting contract to: {ip_addr}')
				with grpc.insecure_channel(ip_addr+':12345') as channel:
					stub = full_node_pb2_grpc.FullNodeStub(channel)
					contract = full_node_pb2.Contract(serialized_contract=serialized_contract,
													broadcast_node=broadcast_node)
					stub.new_contract_broadcast(contract)

	def generate_and_broadcast_contract(self):
		"""Constantly generates and broadcasts contracts
		to other known peers in the network.
		"""
		while True:
			time.sleep(random.uniform(2, 5))
			# generate contract
			contract = self.generate_contract()
			broadcasting_node = get_ip()	# broadcasting node's ip address
			# broadcast new transaction to other peers in the network.
			self.broadcast_contract(contract, broadcasting_node)

	def generate_transaction(self):
		"""Generate two new transaction objects per contract.

		   Only one out of the two transactions will be validated
		   as True (1).
		   The other transaction deemed as False (0) will be deleted
		   from the transaction memory pool.
		"""
		contract = self.contract_pool.get_contract()
		if contract is None:
			return -1, -1
		# user accepts bet and generates two transactions.
		txn_1, txn_2 = self.user.accept_bet(contract)
		# add to memory pool
		self.txn_pool.add_transaction(txn_1)
		self.txn_pool.add_transaction(txn_2)
		print('++++++++++++++++++++++++++++++++++++++++++++')
		print('Generated transactions:')
		print(f'{txn_1.transaction_hash}')
		print(f'{txn_2.transaction_hash}')
		print(f'TRANSACTION MEMORY POOL SIZE: {len(self.txn_pool.list)}')
		print('++++++++++++++++++++++++++++++++++++++++++++')
		return txn_1, txn_2

	def broadcast_transaction(self, transaction, broadcast_node):
		"""Broadcast newly generated transaction.
		"""
		serialized_txn = pickle.dumps(transaction)
		for ip_addr in self.known_peers_list:
			if ip_addr != broadcast_node:
				print(f'Broadcasting transaction to: {ip_addr}')
				with grpc.insecure_channel(ip_addr+':12345') as channel:
					stub = full_node_pb2_grpc.FullNodeStub(channel)
					txn = full_node_pb2.Transaction(serialized_transaction=serialized_txn,
													broadcast_node=broadcast_node)
					stub.new_transaction_broadcast(txn)
	
	def new_transaction_broadcast(self, request, context):
		"""Receives new transaction from other nodes and if the transaction is
		new to the receiving node, the transaction is also broadcasted
		to the remaining nodes in the network.
		
		Note: If the received transaction is new to the node, add to memory pool and
		broadcast that transaction to other nodes, excluding the node that
		broadcasted the said transaction.
		"""
		# ip address of the node that first broadcasted the transaction.
		broadcast_node = request.broadcast_node
		# instantiate transaction object
		transaction = pickle.loads(request.serialized_transaction)
		print(f'Received transaction from: {broadcast_node}')
		need_to_broadcast = True
		# if the received transaction already exists in the memory pool, do nothing
		try:
			for txn in self.txn_pool.list:
				if transaction.transaction_hash == txn.transaction_hash:
					print(f'Transaction already exists in memory pool: {transaction.transaction_hash}')
					need_to_broadcast = False
		except:
			pass
		response = full_node_pb2.txn_broadcast_reply(message="broadcast received")
		return response
	
	def generate_and_broadcast_txn(self):
		"""Constantly generates and broadcasts transactions
		to other known peers in the network.
		"""
		while True:
			time.sleep(random.randint(2, 5))
			# generate transaction
			txn1, txn2 = self.generate_transaction()
			if txn1 == -1 and txn2 == -1:
				continue
			broadcasting_node = get_ip()	# broadcasting node's ip address
			# broadcast new transaction to other peers in the network.
			self.broadcast_transaction(txn1, broadcasting_node)
			self.broadcast_transaction(txn2, broadcasting_node)

	def validate_transaction_add_to_valid_list(self):
		while True:
			for txn in self.txn_pool.list:
				txn.validate_transaction()
			self.txn_pool.update_valid_transaction_list()


def current_time():
	return time.time()

def get_ip():
	"""Returns IP address of client node.

	reference: https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
	"""
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP

def run():
	"""Run Full Node service.
		- listens to port 12345 for incoming handshakes, broadcasts, and contracts
		- broadcasts new transactions that are generated via multithreading
		- broadcasts new blocks that are mined via multithreading

	"""
	full_node = FullNode()
	print(f"\nFull Node IP Address: {get_ip()}\n")
	
	"""
	1) listen to port 12345 for incoming handshakes and broadcasts
	"""
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	full_node_pb2_grpc.add_FullNodeServicer_to_server(full_node, server)
	server.add_insecure_port('[::]:12345')
	server.start()

	"""
	2) Register with DNS_SEED server and receive a null response or
	a single ip address of the latest registered node in the network.
	
	If the response is an ip address, initiate handshake with that node.
	"""
	with grpc.insecure_channel('dns_seed:50051') as channel:
		stub = registrar_pb2_grpc.RegistrarStub(channel)
		# registration response can be null or single ip address)
		response = stub.register(
			registrar_pb2.reg_request(nVersion=1, nTime=current_time(),	addrMe=get_ip())
			)
	# if the dns_seed server returns 'null' for ip address
	if len(response.message) == 0:
		print("Latest registered node IP address: null\n")
	# if the dns_seed server returns a valid ip address of the latest registered node
	else:
		print("Latest registered node IP address: " + response.message[0])
		if response.message[0] not in full_node.known_peers_list:
			full_node.known_peers_list.append(response.message[0])
		# request handshake to the latest registered node
		hs_response = full_node.request_handshake(response.message[0])
		# request handshake to newly known peers
		for ip_addr in hs_response:
			if ip_addr not in full_node.known_peers_list and ip_addr != get_ip():
				full_node.known_peers_list.append(ip_addr)
				full_node.request_handshake(ip_addr)
	
	"""
	3) Generate contracts and broadcast them to other peers in the network.
	"""
	print('... BEGIN GENERATING AND BROADCASTING CONTRACTS ...')
	contract_broadcast = threading.Thread(target=full_node.generate_and_broadcast_contract)
	contract_broadcast.start()

	"""
	4) Generate 2 transactions per accepted contract and broadcast both transactions
	to other peers in the network.
	"""
	print('... BEGIN GENERATING AND BROADCASTING TRANSACTIONS ...')
	txn_broadcast = threading.Thread(target=full_node.generate_and_broadcast_txn)
	txn_broadcast.start()

	"""
	5) Validate transactions and add validated transactions to the 
	valid transaction memory pool.
	"""
	print('... BEGIN ATTEMPTING TO RESOLVE OUTCOMES OF TRANSACTIONS ...')
	validate_txn = threading.Thread(target=full_node.validate_transaction_add_to_valid_list)
	validate_txn.start()

	"""
	5) Mine new blocks and broadcast them to other peers in the network.
	"""
	print('... BEGIN MINING AND BROADCASTING NEW BLOCKS ...')
	mine_thread = threading.Thread(target=full_node.mine_and_broadcast_new_block)
	mine_thread.start()

	"""
	6) Press ctrl+c to stop the server.
	"""
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

if __name__ == '__main__':
	run()