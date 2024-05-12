import time
import hashlib


GENESIS_DATA = {
    "index": 0,
    "timestamp": 1,
    "last_hash": "genesis_last_hash",
    "hash": "genesis_hash",
    "data": [],
}

# check index is equal to 0
# check data is length is equal to 0


class Block:
    """
    Block: a unit of storage
    Store transaction in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, index, timestamp, last_hash, hash, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.last_hash = last_hash
        self.hash = hash

    def calculate_hash(self, index, timestamp, data, last_hash):
        """
        Generate a hash for the block using the given index, timestamp, data, and last_hash and and a sha256 alqorithm
        """
        block_data = str(index) + str(timestamp) + str(data) + str(last_hash)
        return hashlib.sha256(block_data.encode()).hexdigest()

    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        return Block(**GENESIS_DATA)

    def mine_block(self, last_block, data):
        """
        Mine a block based on the given last_block and data
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        index = last_block.index + 1
        hash = self.calculate_hash(self, index, timestamp, data, last_hash)
        return Block(index, timestamp, last_hash, hash, data)

    def __repr__(self):
        return (
            "Block("
            f"index: {self.index},"
            f"timestamp: {self.timestamp},"
            f"last_hash: {self.last_hash},"
            f"hash: {self.hash},"
            f"data: {self.data}"
            ")"
        )
