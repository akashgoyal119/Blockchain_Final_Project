import time
from hashlib import sha256


class Contract:
    """Class representing Contract (bets made by users on a sports game).
    """

    def __init__(self, event, team, quantity, expiration_date, odds,
                 source_of_truth, check_result_time, public_key, digital_sig=''):
        self.event = event
        self.team = team
        self.quantity = int(quantity)
        self.expiration_date = expiration_date
        self.odds = float(odds)
        self.source_of_truth = source_of_truth
        self.check_result_time = check_result_time
        self.party1_public_key = public_key
        self.party1_digital_sig = digital_sig
        self.created_time = time.time()
    
    @property
    def contract_hash_value(self):
        """Compute contract hash value.
        """
        joint = self.event + self.team + str(self.quantity) + str(self.expiration_date) + \
                str(self.odds) + self.source_of_truth + str(self.check_result_time) + \
                self.party1_public_key + self.party1_digital_sig + str(self.created_time)
        return sha256(joint.encode('utf-8')).hexdigest()

    def __repr__(self):
        created_time = str(time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.localtime(self.created_date)))
        expiration_time = str(time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.localtime(self.expiration_date)))
        check_result_time = str(time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.localtime(self.check_result_time)))
        rep = '\n======= PRINT CONTRACT =======\n'
        rep += f'Event: {self.event}\n'
        rep += f'Team: {self.team}\n'
        rep += f'Quantity: {self.quantity}\n'
        rep += f'Odds: {self.odds}\n'
        rep += f'Source of Truth: {self.source_of_truth}\n'
        rep += f'Created Time: {created_date}'
        rep += f'Expiration Time: {expiration_time}\n'
        rep += f'Check Result Time: {check_result_time}\n'
        rep += f'Contract Hash: {self.contract_hash_value}\n'
        rep += '======= END OF CONTRACT =======\n'
        return rep