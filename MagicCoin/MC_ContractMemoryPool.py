# MPCS 56600 - Introduction to Blockchain


from MagicCoin.MC_Contract import Contract
from MagicCoin.MC_User import User
import uuid


class ContractMemoryPool:
    """Class representing Contract Memory Pool in
    """

    def __init__(self, number_of_contract):
        """Initialize ContractMemoryPool object.
        
        Note: Default number of contract is 91 as given in the
        instructions.
        """
        try:
            assert(type(number_of_contract) is int)
            self.list = self.fill_contract_memory_pool(number_of_contract)
        except:
            print('Error: number_of_contract must be in int.')
            raise


    def fill_contract_memory_pool(self, number_of_contract):
        """Fill the contract memory pool with randomly
        generated contract objects.
        """
        # generate random public key.
        public_key = str(uuid.uuid4())
        user = User(public_key=public_key)
        contract_list = []
        for i in range(number_of_contract):
            contract_list.append(user.generate_random_contract())
        return contract_list

    def size(self):
        """Returns the size of the pool.
        """
        return len(self.list)

    def get_contract(self, idx=0):
        """Returns the oldest contract object in the pool.
        """
        if self.size() == 0:
            return None
        try:
            # remove and return the oldest contract object in the pool
            contract = self.list.pop(idx)
            return contract
        except:
            return f'Error: Index must be an integer in range [0, {self.size()-1}]'
    
    def add_contract(self, contract):
        """Adds a contract object to the pool.
        """
        try:
            assert(type(contract) == Contract)
            return self.list.append(contract)
        except:
            return 'Type Error: Must add contract object.'

    def get_contract_by_hash(self, contract_hash):
        for contract in self.list:
            if contract.contract_hash_value == contract_hash:
                return contract
        return "Contract does not exist."
