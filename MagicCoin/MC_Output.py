# MPCS 56600 - Introduction to Blockchain
# Jae-Yeun Hwang

# Lab 5
# Problem 1

import random, string


class Output:
    """Class representing Transaction Output in MagicCoin.
    """

    def __init__(self, value, public_address, digital_sig):
        """Initialize Output object.
        """
        # the lowest value for MagicCoins is called quidditch.
        self.value = int(value)
        self.public_address = str(public_address)
        self.digital_sig = str(digital_sig)

    @classmethod
    def generate_output(cls, value):
        """Returns Output object.
        """
        public_address = Output.generate_random_script(32)
        digital_sig = Output.generate_random_script(32)
        return cls(value, public_address, digital_sig)

    @staticmethod
    def generate_random_value(l_bound, u_bound):
        """Returns random value in 'quidditch', which is the
        smallest unit for MagicCoin.
        """
        return int(random.randint(l_bound, u_bound))

    @staticmethod
    def generate_random_script(script_length):
        """Returns random string for script in Output object.
        """
        # reference: https://pythontips.com/2013/07/28/generating-a-random-string/
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(script_length)])

    def __repr__(self):
        output = f'value: {self.value}\n'
        output += f'public_address: {self.public_address}\n'
        output += f'digital_sig: {self.digital_sig}'
        return output

