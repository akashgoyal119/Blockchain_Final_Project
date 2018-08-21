from hashlib import sha256
from binascii import unhexlify, hexlify
from MagicCoin.MC_Transaction import Transaction
from MagicCoin.MC_Output import Output
from MagicCoin.MC_Contract import Contract
from MagicCoin.MC_User import User
from MagicCoin.MC_Header import Header
import sys
import random
import time


class Block:
    """Class representing Block in
    """
    # MAX_TXNS field
    MAX_TXNS = 10

    def __init__(self, hash_prev_block_header, transactions, magic_number=0xD9B4BEF9):
        """Initialize Block object.

            transactions is a list of Transaction obj.
            magic_number is constant.
            hash_prev_block_header is needed to initialize Header object.
            transactions is used to compute Merkle Root.
        """
        self.magic_number = magic_number
        # reference: https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
        self.blocksize = sys.getsizeof(self)
        self.transactions_list = transactions # list of Transaction objects
        self.transactions = self.transactions_dic() # dictionary
        self.transaction_counter = len(self.transactions)
        self.hash_prev_block_header = hash_prev_block_header
        # initialize Header object
        self.block_header = Header(self.hash_prev_block_header, self.merkle_root())
        self.txids_list = [t.transaction_hash for t in self.transactions_list]
        self.block_number = 0

    def block_hash(self):
        """Compute block hash.
        """
        h = self.block_header
        return h.hash_block_header()

    def transactions_dic(self):
        """Return dictionary of transaction ids and transactions.
        """
        transactions_dic = {}
        
        for t in self.transactions_list:
            transactions_dic[t.transaction_hash] = t
        return transactions_dic

    def compute_depth(self, num_nodes, depth=0):
        """Recursively computes and returns the depth of Merkle Tree.
        """
        if num_nodes == 0 or num_nodes == 1:
            return 0
        else:
            # lower bound for number of nodes for merkle tree by depth
            l_bound = 2 ** (depth-1) + 1
            # upper bound for number of nodes for merkle tree by depth
            u_bound = 2 ** depth
            if num_nodes >= l_bound and num_nodes <= u_bound:
                return depth
            else:
                # recursively checks if the depth is correct
                # after incrementing depth by 1
                depth += 1
                return self.compute_depth(num_nodes, depth)

    def reverse_hash_value(self, hash_value):
        """Reverse hash value.
        """
        b_array = bytearray(hash_value)
        b_array.reverse()
        reversed_hex = hexlify(b_array)
        return reversed_hex
    
    def hash_two_value(self, value1, value2):
        """Returns sha256 hash value of two input value.
        """
        reversed_1 = self.reverse_hash_value(unhexlify(value1))
        reversed_2 = self.reverse_hash_value(unhexlify(value2))
        reversed_concat = reversed_1 + reversed_2
        reversed_unhex = unhexlify(reversed_concat)
        reversed_hash = sha256(sha256(reversed_unhex).digest()).digest()
        hash_value = self.reverse_hash_value(reversed_hash).decode('utf-8')
        return hash_value
    
    def merkle_root(self):
        """Compute merkle root.
        """
        txids_list = [t.transaction_hash for t in self.transactions_list]
        num_nodes = len(txids_list)
        depth = self.compute_depth(num_nodes)
        while depth > 0:
            if num_nodes % 2 == 0:
                # list that stores computed hash value (parent node)
                hash_value_list = []
                for i in range(1, num_nodes+1, 2):
                    hash_value = self.hash_two_value(txids_list[i-1], txids_list[i])
                    hash_value_list.append(hash_value)
                txids_list = hash_value_list
                num_nodes = len(txids_list)
                depth -= 1
            # if number of nodes at depth is not even, append the last
            # hash value to the transaction id list to make the number
            # of nodes even.
            else:
                txids_list.append(txids_list[-1])
                num_nodes = len(txids_list)
        return txids_list[0]

    def __repr__(self):
        """Representation of Block object.
        """
        rep = '\n======= PRINT BLOCK =======\n'
        rep += f'MagicNumber: {self.magic_number}\n'
        rep += f'Blocksize: {self.blocksize}\n'
        rep += f'BlockHeader: {self.block_header}\n'
        rep += f'TransactionCounter: {self.transaction_counter}\n'
        rep += f'Transactions (Transaction Hash): {", ".join(self.txids_list)}\n'
        rep += f'BlockHash: {self.block_hash()}\n'
        rep += '======= END OF BLOCK =======\n'
        return rep

    def print_block(self):
        print(self)

    @classmethod
    def generate_genesis_block(cls):
        """Generate genesis block for the blockchain in MagicCoin.
        """
        first_user = User('Harry Potter')
        #genesis_contract = first_user.generate_random_contract()
        event = "Gryffindor vs Slytherin"
        team = "Gryffindor"
        quantity = 100000
        expiration_date = int(time.time())
        odds = 0.1
        source_of_truth = "Albus Dumbledore"
        check_result_time = int(time.time())
        genesis_contract = Contract(event, team, quantity, expiration_date, odds, source_of_truth, check_result_time,
                            first_user.public_key)
        input_1 = Output(value=genesis_contract.quantity,
                         public_address=genesis_contract.party1_public_key,
                         digital_sig=genesis_contract.party1_digital_sig)
        output_1 = Output(value=genesis_contract.quantity-50,
                           public_address=genesis_contract.party1_public_key,
                           digital_sig=genesis_contract.party1_digital_sig)
        genesis_transaction = [Transaction(input_1, output_1, genesis_contract)]
        return cls('0' * 64, genesis_transaction)

