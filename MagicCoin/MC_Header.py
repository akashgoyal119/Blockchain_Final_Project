from hashlib import sha256
from binascii import unhexlify, hexlify
import time


class Header:
    """Class representing Header in MagicCoin.
    """

    def __init__(self, hash_prev_block, hash_merkle_root, bits=0x1e200000, nonce=0, version_num=1):
        """Initialize Header object.

           default difficulty bits = 0x207fffff
           version_num is constant.
        """
        self.version_num = int(version_num)
        self.hash_prev_block_header = hash_prev_block
        self.hash_merkle_root = hash_merkle_root
        self.timestamp = int(time.time())
        self.bits = int(bits)
        self.nonce = int(nonce)

    def hash_block_header(self):
        """Returns hash (byte object) of the concatentated fields of
           version number, hash prev block header, hash merkle root,
           timestamp, bits, nonce.
        """
        # concatenate all the fields into string
        string = str(self.timestamp)
        string += self.hash_merkle_root
        string += str(self.bits)
        string += str(self.nonce)
        string += self.hash_prev_block_header
        hash_value = sha256(sha256(string.encode()).hexdigest().encode()).hexdigest()
        return hash_value

    def __repr__(self):
        """Representation of Header object.
        """
        rep = '\n======= PRINT BLOCK HEADER =======\n'
        rep += f'VersionNumber: {self.version_num}\n'
        rep += f'hashPrevBlock: {self.hash_prev_block_header}\n'
        rep += f'hashMerkleRoot: {self.hash_merkle_root}\n'
        rep += f'Timestamp: {self.timestamp}\n'
        rep += f'Bits: {self.bits}\n'
        rep += f'Nonce: {self.nonce}\n'
        rep += '======= END OF BLOCK HEADER ======='
        return rep

    def print_header(self):
        print(self)