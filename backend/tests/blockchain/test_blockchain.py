from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import Block, GENESIS_DATA

import pytest  # type: ignore


class TestBlockchain:
    self = Blockchain

    @pytest.fixture
    def add_block(self):
        """
        Fixture to add a block to a Blockchain object for testing.
        This fixture creates a new instance of a `Blockchain` object and adds a block with test data to it.
        The `yield` statement allows the test to access both the blockchain and the test data.
        Yields:
            tuple: A tuple containing the `Blockchain` object and the test data.
        """
        blockchain = Blockchain()
        data = "test-data"
        blockchain.add_block(data)
        yield blockchain, data

    def test_blockchain(self):
        """
        Unit test for the Blockchain constructor.
        The test verifies that the `Blockchain` constructor creates an instance of the `Blockchain` class.
        It checks if the created `blockchain` object is an instance of the `Blockchain` class using the `isinstance` function.
        """
        blockchain = Blockchain()
        assert isinstance(blockchain, Blockchain)

    def test_blockchain_instance(self):
        """
        Unit test for the Blockchain instance.
        The test verifies that the `Blockchain` instance initializes with the expected genesis block.
        It checks if the hash of the first block in the `blockchain` matches the hash value defined in `GENESIS_DATA`.
        """
        blockchain = Blockchain()
        assert blockchain.chain[0].hash == GENESIS_DATA["hash"]

    def test_add_block(self, add_block):
        """
        Unit test for the add_block method of the Blockchain class.
        The test verifies that the `add_block` method adds a new block to the `Blockchain` object.
        It uses the `add_block` fixture to obtain a `Blockchain` instance and test data.
        The test then checks if the data of the last block in the blockchain matches the provided test data.
        Args:
            add_block (fixture): The add_block fixture that provides a `Blockchain` object and test data.
        """
        blockchain, data = add_block
        assert blockchain.chain[-1].data == data

    def test_repr(self, add_block):
        """
        Unit test for the __repr__ method of the Block class.
        The test verifies the string representation (__repr__) of a Block object in the Blockchain.
        It uses the add_block fixture to obtain a Blockchain instance and a test block.
        The test then checks if the representation of the first block in the blockchain matches the expected representation.
        Args:
        add_block (fixture): The add_block fixture that provides a Blockchain object and test data.
        """
        blockchain, _ = add_block
        expected_repr = "Block(index: 0,timestamp: 1,last_hash: genesis_last_hash,hash: genesis_hash,data: [])"
        assert repr(blockchain.chain[0]) == expected_repr
