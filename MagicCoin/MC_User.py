from hashlib import sha256
import time
import random, string

from MagicCoin.MC_Contract import Contract
from MagicCoin.MC_Transaction import Transaction
from MagicCoin.MC_TxnMemoryPool import TxnMemoryPool
from MagicCoin.MC_Output import Output


class User:

    def __init__(self, public_key, balance = 1000000000):
        self.public_key = public_key
        self.balance = balance

    def generate_random_contract(self):
        """Generate random contract to simulate mining.
        """
        team_a = str(Output.generate_random_script(5))
        team_b = str(Output.generate_random_script(5))
        event = team_a + " vs " + team_b
        team = team_a
        quantity = Output.generate_random_value(1000, 5000)
        current_time = time.time()
        expiration_date = current_time + 1
        odds = float(random.random() * 2.0)
        source_of_truth = 'www.espn.com'
        check_result_time = current_time + 2
        contract = Contract(event, team, quantity, expiration_date, odds, source_of_truth, check_result_time,
                            self.public_key)
        dig_sig = sha256((self.public_key + str(time.time()) + contract.contract_hash_value).encode('utf-8')).hexdigest()
        contract.party1_digital_sig = dig_sig
        
        # contract_memory_pool.add_contract(contract)
        # will need to figure out method to broadcast this after creation
        return contract

    def accept_bet(self, contract_hash_value, contract_memory_pool, txn_memory_pool):
        contract = contract_memory_pool.get_contract_by_hash(contract_hash_value)
        dig_sig2 = sha256((self.public_key + str(time.time())).encode('utf-8')).hexdigest()

        #  txn :   def __init__(self, input, output, contract):
        #  output :     def __init__(self, value, public_address, digital_sig):

        # contract: def __init__(self, event, team, quantity, expiration_date, odds,
        #         source_of_truth, check_result_time, public_key, digital_sig):

        money_paid_by_the_better = contract.quantity * contract.odds
        money_paid_by_the_receiver = contract.quantity
        input_1 = Output(value=money_paid_by_the_better,
                         public_address=contract.party1_public_key,
                         digital_sig=contract.party1_digital_sig)
        output_1 = Output(value=money_paid_by_the_better - 50,
                          public_address=self.public_key,
                          digital_sig=dig_sig2)

        txn_1 = Transaction(input_1, output_1, contract)
        
        # in later version txn2 should be the opposite team as txn1.
        input_2 = Output(value=money_paid_by_the_receiver,
                         public_address=self.public_key,
                         digital_sig=dig_sig2)

        output_2 = Output(value=money_paid_by_the_receiver - 50,
                          public_address=contract.party1_public_key,
                          digital_sig=contract.party1_digital_sig)

        txn_2 = Transaction(input_2, output_2, contract)

        txn_memory_pool.add_transaction(txn_1)
        txn_memory_pool.add_transaction(txn_2)


        # TODO: need to broadcast

