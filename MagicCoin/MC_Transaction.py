import random
import time
import json
from MagicCoin.MC_Output import Output
from MagicCoin.MC_Contract import Contract
from hashlib import sha256


class Transaction:
    """Class representing Transaction in MagicCoin.
    """
    # avg_transaction_fee per transaction
    avg_transaction_fee = int(50)
    # coinbase reward is 50 MagicCoins
    coinbase_reward = int(50000)

    def __init__(self, input, output, contract):
        self.input = input
        self.output = output
        self.is_valid = None
        self.contract = contract

    def validate_transaction(self):
        """After each contract's check_result_time, which is the
           time when the outcome of the contract (bet) is determined,
           only one of the two transactions created per contract will
           be validated (is_valid = 1) and will be added to the 
           valid transaction memory pool, which will eventually be
           mined into blockchain.

           The other transaction that has 'is_valid = 0' will be deleted
           from the transaction memory pool
        """
        if time.time() < self.contract.check_result_time:
            return None
        else:
            if self.is_valid is None:
                # Fake criteria for transaction validation for simulation purposes.
                # The fake criteria must be deterministic since each node must evaluate the
                # same transactions as valid.
                # In real life, the "is_valid" field will be determined by the outcome
                # of the actual sports game or bet.
                if self.input.value == self.contract.quantity:
                    self.is_valid = 1
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(f'Transaction validated: {self.transaction_hash}')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                else:
                    self.is_valid = 0

    @property
    # the odds should be implemented as a float, so for example, a bet of $10 with odds 0.5 implies that
    # the posting better will win $5 if he wins or lose $10 if he loses.
    # If odds are 1.5, posting better wins $15 if he wins or loses $10 if he loses
    def money_paid_by_the_better(self):
        return self.contract.quantity * self.contract.odds
    
    @property
    def money_paid_by_the_receiver(self):
        return self.contract.quantity
    
    @property
    def transaction_hash(self):
        serialize_input = json.dumps(self.input, default=lambda x: x.__dict__)
        serialize_output = json.dumps(self.output, default=lambda x: x.__dict__)
        string = serialize_input + serialize_output + self.contract.contract_hash_value
        return sha256(string.encode('utf-8')).hexdigest()

    @classmethod
    def generate_coinbase_transaction(cls, total_transaction_fee):
        """Generate coinbase Transaction object that includes the
           reward for the miner.

           transaction_list: list of Transaction obj to be included
           in the new block
        """
        input_value = 0
        input_obj = Output.generate_output(input_value)
        # coinbase reward is 50000 MagicCoins
        output_value = cls.coinbase_reward
        # aggregate transaction fee of the transactions that will
        # be included in the new block.
        output_value += total_transaction_fee
        public_key = 'CONGRATS YOU WON THE COINBASE REWARD!!!'
        digtal_sig = input_obj.digital_sig
        output_obj = Output(output_value, public_key, digtal_sig)
        coinbase_contract = Contract('Coinbase Contract','Coinbase',output_value,'Coinbase',1,'Coinbase',
                    'Coinbase','Coinbase','Coinbase') 
        return cls(input_obj, output_obj, coinbase_contract)

    def transaction_fee(self):
        """Returns transaction fee for a Transaction obj in quidditch.
        """
        transaction_fee = self.input.value - self.output.value
        return transaction_fee

    def __repr__(self):
        """Representation of Transaction object.
        """
        check_result_time = str(time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.localtime(self.contract.check_result_time)))
        rep = '\n======= PRINT TRANSACTION =======\n'
        rep += f'1) Input: {self.input}\n'
        rep += f'2) Output: {self.output}\n'
        rep += f'3) Is_Valid: {self.is_valid}\n'
        rep += f'4) Contract Hash: {self.contract.contract_hash_value}\n'
        rep += f'5) Contract Source of Truth: {self.contract.source_of_truth}\n'
        rep += f'6) Contract Check Result Time: {check_result_time}\n'
        rep += '======= END OF TRANSACTION =======\n'
        return rep
