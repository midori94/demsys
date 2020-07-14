from hashlib import sha256
import json

class block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
 
    def compute_hash(self):
        """
        A function that return the hash of the block content.
        """
        block_string = json.dumps(self.__dict__, sort_keys = True)
        return sha256(block_string.encode()).hexdigest()

if __name__ == "__main__":
    new_block = block(1, "hola", "now", "previous_hash")
    print(new_block.compute_hash())


