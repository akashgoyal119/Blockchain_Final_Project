# MPCS 56600 - Introduction to Blockchain
# Jae-Yeun Hwang

# Lab 5
# Problem 1


from MagicCoin.MC_Transaction import Transaction


class TxnMemoryPool:
    """Class representing Transaction Memory Pool in MagicCoin.
    """

    def __init__(self, number_of_txn=0):
        """Initialize TxnMemoryPool object.
        
        Note: Default number of transactions is 91 as given in the
        instructions.
        """
        try:
            assert(type(number_of_txn) is int)
            self.list = self.fill_txn_memory_pool(number_of_txn)
        except:
            return 'Error: number_of_txn must be in int.'

    def fill_txn_memory_pool(self, number_of_txn):
        """Fill the transaction memory pool with randomly
        generated Transaction objects.
        """
        transaction_list = []
        for i in range(number_of_txn):
            transaction_list.append(Transaction.generate_transaction())
        return transaction_list

    def size(self):
        """Returns the size of the pool.
        """
        return len(self.list)

    def get_transaction(self, idx=0):
        """Returns the oldest Transaction object in the pool.
        """
        if self.size() == 0:
            return None
        try:
            # remove and return the oldest Transaction object in the pool
            txn = self.list.pop(idx)
            return txn
        except:
            return f'Error: Index must be an integer in range [0, {self.size()-1}]'
    
    def add_transaction(self, transaction):
        """Adds a Transaction object to the pool.
        """
        try:
            assert(type(transaction) == Transaction)
            return self.list.append(transaction)
        except:
            return 'Type Error: Must add Transaction object.'