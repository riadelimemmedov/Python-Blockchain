from backend.blockchain.block import Block, GENESIS_DATA

import pytest  # type: ignore


class TestBlock:
    self = Block

    @pytest.fixture
    def block(self):
        """
        Fixture to create a sample Block object for testing.
        Returns:
            Block: A sample Block object with predefined attributes for testing purposes.
        """
        index = 1
        timestamp = "2022-01-01 12:00:00"
        last_hash = "previous_hash"
        hash = "current_hash"
        data = "Hello, world!"
        yield Block(
            index=index, timestamp=timestamp, last_hash=last_hash, hash=hash, data=data
        )

    def test_calculate_hash(self):
        """
        Test the calculate_hash() method of the Block class.
        This test checks that the calculate_hash() method correctly calculates the hash of a Block object.
        """
        index = 1
        timestamp = 1620734400  # May 11, 2021, 00:00:00 (Unix timestamp)
        data = "Hello, world!"
        last_hash = "previous_hash"

        calculated_hash = Block.calculate_hash(
            TestBlock.self, index, timestamp, data, last_hash
        )
        assert calculated_hash == calculated_hash
        assert len(calculated_hash) == 64

    def test_mine_block(self):
        """
        Unit test for the mine_block method.
        The method tests the mining of a new Block object using a previous block and test data.
        It verifies that the mined block is an instance of the Block class, has a non-zero timestamp in milliseconds,
        has a last_hash value equal to the hash of the previous block, has an index value that is one greater than the index of the previous block,
        and has a data value equal to the provided test data.
        """
        last_block = Block.genesis()
        data = "test-data"
        block = Block.mine_block(TestBlock.self, last_block, data)
        assert isinstance(block, Block)
        assert block.timestamp % 1000 != 0
        assert block.last_hash == last_block.hash
        assert last_block.index == block.index - 1
        assert block.data == data

    def test_genesis(self):
        """
        Unit test for the genesis method.
        The method tests the creation of the genesis Block object.
        It verifies that the generated genesis block is an instance of the Block class,
        has an index and data length equal to 0, and has attribute values matching the predefined GENESIS_DATA.
        """
        genesis = Block.genesis()
        assert isinstance(genesis, Block)
        assert (genesis.index and len(genesis.data)) == 0
        assert all(
            getattr(genesis, attr) == GENESIS_DATA[attr] for attr in GENESIS_DATA
        )

    def test_repr(self, block):
        """
        Unit test for the __repr__ method.
        The method tests the string representation (__repr__) of a Block object.
        It verifies that the generated representation matches the expected representation.
        """
        expected_repr = "Block(index: 1,timestamp: 2022-01-01 12:00:00,last_hash: previous_hash,hash: current_hash,data: Hello, world!)"
        assert repr(block) == expected_repr
