# MPCS 56600 - Introduction to Blockchain
# Team project

import time
from hashlib import sha256


class Contract:

    def __init__(self, event, team, quantity, expiration_date, odds,
                 source_of_truth, check_result_time, public_key, digital_sig):
                
        self.event = event
        self.team = team
        self.quantity = int(quantity)
        self.expiration_date = expiration_date
        self.odds = float(odds)
        self.source_of_truth = source_of_truth
        self.check_result_time = check_result_time
        self.party1_public_key = public_key
        self.party1_digital_sig = digital_sig
        self.current_time = str(time.time()) 
    
    @property
    def contract_hash_value(self):
        joint = self.event + self.team + str(self.quantity) + str(self.expiration_date) + \
                str(self.odds) + self.source_of_truth + str(self.check_result_time) + \
                self.party1_public_key + self.party1_digital_sig + str(self.current_time)
        return sha256(joint.encode('utf-8')).hexdigest()

    def __repr__(self):
        return self.contract_hash_value