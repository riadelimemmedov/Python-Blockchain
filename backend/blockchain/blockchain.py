from .block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """

    def __init__(self):
        self.block = Block
        self.chain = [self.block.genesis()]

    def validate_blockchain(self):
        for index in range(len(self.chain) - 1):
            yield self.chain[index].hash == self.chain[index + 1].last_hash

    def add_block(self, data):
        if self.validate_blockchain():
            self.chain.append(self.block.mine_block(self.block, self.chain[-1], data))

    def __repr__(self):
        return f"Blockchain - {self.chain}"


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("data1")
    blockchain.add_block("data2")
    blockchain.add_block("data3")
