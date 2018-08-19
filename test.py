from MagicCoin.MC_Block import Block
from MagicCoin.MC_BlockChain import BlockChain
from MagicCoin.MC_Contract import  Contract
from MagicCoin.MC_Output import Output
from MagicCoin.MC_ContractMemoryPool import ContractMemoryPool
from MagicCoin.MC_Output import Output
from MagicCoin.MC_Transaction import Transaction
from MagicCoin.MC_TxnMemoryPool import TxnMemoryPool
from MagicCoin.MC_User import User
from MagicCoin.MC_Miner import Miner
from MagicCoin.MC_Header import Header
import time
import uuid


def main():
    # generate contract
    contract_pool = ContractMemoryPool(100)
    
    txn_memory_pool = TxnMemoryPool()

    # fill transaction memory pool
    public_key = str(uuid.uuid4())
    user_1 = User(public_key=public_key)
    for contract in contract_pool.list:
       user_1.accept_bet(contract.contract_hash_value, contract_pool, txn_memory_pool)

    print('sleep for 3 seconds')
    time.sleep(3)

    # fill valid transaction memory pool
    for txn in txn_memory_pool.list:
        txn.validate_transaction()
    txn_memory_pool.update_valid_transaction_list()
    #print(txn_memory_pool.valid_list)

    # Get ready to mine some MagicCoins!!!
    miner = Miner()
    # generate genesis block
    genesis_block = Block.generate_genesis_block()
    #print(genesis_block)

    # initialize BlockChain object (first block is genesis block)
    blockchain = BlockChain(genesis_block)

    # recursively mine blockchain
    blockchain = miner.mine_blockchain(blockchain, txn_memory_pool)



if __name__ == '__main__':
    main()
