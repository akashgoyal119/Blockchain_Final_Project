# MPCS 56600 - Introduction to Blockchain


from MagicCoin.MC_Block import Block
from MagicCoin.MC_Header import Header
from MagicCoin.MC_Transaction import Transaction
from MagicCoin.MC_TxnMemoryPool import TxnMemoryPool


class Miner:
    """Class representing Miner object in
    """
    def __init__(self):
        pass
    
    def get_target_from_bits(self, bits):
        """Codes from diff_calc.2.py provided by the instructor.
        """
        if type(bits) == str:
            bits = int(bits)
        shift = bits >> 24
        value = bits & 0x007fffff
        value <<= 8 * (shift - 3)
        return value

    def mine_new_block(self, prev_block, new_block_txn_list):
        """Mines new block.

        Args:
            hash_prev_block_header: hash value of previous block header
        """
        total_txn_fee = 0
        for txn in new_block_txn_list:
            total_txn_fee += txn.transaction_fee()
        print('================================')
        print('Mining New Block')
        print('================================')
        # generate coinbase_transaction
        coinbase_txn = Transaction.generate_coinbase_transaction(total_txn_fee)
        # add this too the txn list
        new_block_txn_list.append(coinbase_txn)
        # get hash value of prev block header
        hash_prev_block_header = prev_block.block_hash()
        # new candidate block
        new_block = Block(hash_prev_block_header, new_block_txn_list)
        # merkle root
        merkle_root = new_block.merkle_root()
        # new candidate block header
        new_block_header = Header(hash_prev_block_header, merkle_root)
        # set target for Proof of Work algorithm
        target = self.get_target_from_bits(new_block_header.bits)
        # convert hex into int
        # reference: https://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python
        while int(new_block_header.hash_block_header(), 16) > target:
            print('Unsuccessful...')
            print(f'Nonce: {new_block_header.nonce}')
            print('Guess : %064x' % (int(new_block_header.hash_block_header(), 16)))
            print('Target: %064x' % target)
            print('')
            #increment nonce by 1 until success
            new_block_header.nonce += 1
        print('--------------------------------')
        print('!!!MINING SUCCESSFUL!!!')
        print(f'Nonce: {new_block_header.nonce}')
        print('Guess : %064x' % (int(new_block_header.hash_block_header(), 16)))
        print('Target: %064x' % target)
        print('--------------------------------')

        new_block_header = Header(hash_prev_block_header, merkle_root, nonce=new_block_header.nonce)
        new_block.block_header = new_block_header
        return new_block, total_txn_fee

    def mine_blockchain(self, blockchain, txn_memory_pool):
        """Recursively mines new blocks and adds them to
        the existing blockchain (or to the genesis block).
        """
        new_block_txn_list = []
        if txn_memory_pool.size() <= 0:
            # if memory pool is empty, return blockchain
            return blockchain
        elif txn_memory_pool.size() <= (Block.MAX_TXNS - 1):
            # if there are less number of txn left than MAX_TXNS
            # create new block with the remaining txns.
            for i in range(txn_memory_pool.size()):
                txn = txn_memory_pool.get_transaction()

                # if transaction is_valid field is true, add to the working memory pool
                if txn.is_valid == 1:
                    new_block_txn_list.append(txn)

            # get prev_block to get the hash value
            prev_block = blockchain.get_most_recent_block()
            # mine new block
            new_block, total_txn_fee = self.mine_new_block(prev_block, new_block_txn_list)
            # add new block to blockchain
            blockchain.add_block(new_block)
            print('New Block added !!!\n')
            print(f'BlockChain Height: {blockchain.height()}')
            print(f'MagicCoin Rewarded (Reward + Transaction Fees): {total_txn_fee} quidditch')
            print('================================')
            return blockchain
        else:
            # create new block by consuming transactions from
            # the txn_memory_pool
            for i in range(Block.MAX_TXNS - 1):
                txn = txn_memory_pool.get_transaction()

                # if transaction is_valid field is true, add to the working memory pool
                if txn.is_valid == 1:
                    new_block_txn_list.append(txn)

            # get prev_block to get the hash value
            prev_block = blockchain.get_most_recent_block()
            new_block, total_txn_fee = self.mine_new_block(prev_block, new_block_txn_list)
            blockchain.add_block(new_block)
            print('New Block added !!!\n')
            print(f'BlockChain height: {blockchain.height()}')
            print(f'MagicCoin Rewarded (Reward + Transaction Fees): {total_txn_fee} quidditch')
            print('================================')
            return self.mine_blockchain(blockchain, txn_memory_pool)
