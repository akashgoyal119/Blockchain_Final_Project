from MagicCoin.MC_Transaction import Transaction


class TxnMemoryPool:
    """Class representing Transaction Memory Pool in MagicCoin.
    """

    def __init__(self, number_of_txn=0):
        """Initialize TxnMemoryPool object.
        
           Default number of transactions is 91 as given in the
           instructions.
        """
        try:
            assert(type(number_of_txn) is int)
            self.list = self.fill_txn_memory_pool(number_of_txn)
        except:
            raise
            return 'Error: number_of_txn must be in int.'
        self.valid_list = []

    def update_valid_transaction_list(self):
        temp_txn_list = []
        for txn in self.list:
            if txn.is_valid == 1:
                self.valid_list.append(txn)
            elif txn.is_valid == 0:
                pass
            else: # unresolved case 
                temp_txn_list.append(txn)
        self.list = temp_txn_list

    def fill_txn_memory_pool(self, number_of_txn):
        """Fill the transaction memory pool with randomly
           generated Transaction objects.
        """
        transaction_list = []
        for i in range(number_of_txn):
            transaction_list.append(Transaction.generate_transaction())
        return transaction_list

    def size(self):
        """Returns the size of the valid transaction pool.
        """
        return len(self.valid_list)

    def get_transaction(self, idx=0):
        """Returns the oldest Transaction object in the pool.
        """
        if self.size() == 0:
            return None
        try:
            # remove and return the oldest Transaction object in the pool
            txn = self.valid_list.pop(idx)
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
