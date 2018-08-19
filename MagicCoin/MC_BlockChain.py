# MPCS 56600 - Introduction to Blockchain
# Jae-Yeun Hwang

# Lab 5
# Problem 1


from MagicCoin.MC_Block import Block


class BlockChain:
    """Class representing BlockChain in MagicCoin.
    """

    def __init__(self, genesis_block):
        """Initialize BlockChain object.
        """
        self.genesis_block = genesis_block
        self.blocks = []
        self.add_block(genesis_block)

    def height(self):
        return len(self.blocks)-1

    def add_block(self, block):
        try:
            assert(type(block) is Block)
            return self.blocks.append(block)
        except:
            return f'Error: Must add Block object.'

    def get_block_by_height(self, h):
        try:
            return self.blocks[h]
        except:
            max_h = len(self.blocks)-1
            return f'Enter an integer value between 0 and {max_h} (inclusive).'
    
    def get_block_by_block_hash(self, hash_value):
        for block in self.blocks:
            if block.block_hash() == hash_value:
                return block
        return f"Block with hash {hash_value} does not exist."
    
    def get_transaction_by_transaction_hash(self, hash_value):
        for block in self.blocks:
            for transaction_hash, transaction in block.transactions.items():
                if transaction_hash == hash_value:
                    return transaction
        return f"Transaction with hash {hash_value} does not exist."

    def get_most_recent_block(self):
        return self.blocks[-1]