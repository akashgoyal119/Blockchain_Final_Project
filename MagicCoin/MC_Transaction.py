import random
import time
import json
from MagicCoin.MC_Output import Output
from hashlib import sha256


class Transaction:

    avg_transaction_fee = int(50)
    # coinbase reward is 50 MagicCoins
    coinbase_reward = int(50000)

    def __init__(self, input, output, contract):
        self.input = input
        self.output = output
        self.is_valid = None
        self.contract = contract

    def determine_outcome(self):
        if time.time() < self.contract.check_result_time:
            return None
        else:
            # we should probably actually implement a better version of this later...
            if not self.is_valid:
                self.is_valid = random.randint(0, 1)

    @property
    # the odds should be implemented as a float, so for example, a bet of $10 with odds 0.5 implies that
    # the posting better will win $5 if he wins or lose $10 if he loses.
    # If odds are 1.5, posting better wins $15 if he wins or loses $10 if he loses
    def money_to_posting_better(self):
        return self.contract.quantity * self.contract.odds
    
    @property
    def money_to_accepting_better(self):
        return self.contract.quantity
    
    @property
    def transaction_hash(self):

        serialize_input = json.dumps(self.input, default=lambda x: x.__dict__)
        serialize_output = json.dumps(self.output, default=lambda x: x.__dict__)
        string = serialize_input + serialize_output + self.contract.contract_hash_value

        return sha256(string.encode('utf-8')).hexdigest()

    # @classmethod
    # def generate_transaction(cls):
    #     """Generate Transaction object with random
    #     value and script.
    #     """
    #     # random value between 1 - 1000 MagicCoin
    #     input_value = Output.generate_random_value(1, 1000000)
    #     # transaction fee is on avg 50 quidditch for MagicCoin
    #     # randomize transaction fee to simulate real life transaction fees
    #     txn_fee = int(cls.avg_transaction_fee*2*random.random())
    #     output_value = input_value - txn_fee
    #     list_of_inputs = Output.generate_output(input_value)
    #     list_of_outputs = Output.generate_output(output_value)
    #     return cls(list_of_inputs, list_of_outputs, )

    @classmethod
    def generate_coinbase_transaction(cls, total_transaction_fee):
        """Generate coinbase Transaction object that includes the
        reward for the miner.

        transaction_list: list of Transaction obj to be included
        in the new block
        """
        # coinbase reward is 50 MagicCoins
        output_value = cls.coinbase_reward
        # aggregate transaction fee of the transactions that will
        # be included in the new block.
        output_value += total_transaction_fee
        public_key = 'CONGRATS YOU WON THE COINBASE REWARD!!!'
        digtal_sig = Output.generate_random_script()

        input_value = Output.generate_random_value(1, 1000000)
        list_of_inputs = Output.generate_output(input_value)

        list_of_outputs = Output(output_value, public_key, digtal_sig)
        return cls(list_of_inputs, list_of_outputs, None)

    def transaction_fee(self):
        """Returns transaction fee for a Transaction obj in quidditch.
        """
        transaction_fee = 0
        for txn_in, txn_out in zip(self.list_of_inputs, self.list_of_outputs):
            transaction_fee += txn_in.value - txn_out.value
        return transaction_fee

