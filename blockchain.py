import hashlib
import json
from time import time
from datetime import datetime


class Block:
    """Represents a single block in the blockchain."""
    
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Initialize a new block.
        
        Args:
            index (int): Position of the block in the chain
            timestamp (float): Time when the block was created
            data (str): Data/transaction stored in the block
            previous_hash (str): Hash of the previous block
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Calculate the SHA-256 hash of the block.
        
        Returns:
            str: Hexadecimal hash string
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def __repr__(self):
        """String representation of the block."""
        return f"Block(index={self.index}, hash={self.hash[:10]}...)"


class Blockchain:
    """Represents the blockchain - a chain of blocks."""
    
    def __init__(self):
        """Initialize the blockchain with a genesis block."""
        self.chain = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        """Create the first block in the blockchain."""
        genesis_block = Block(0, time(), "Genesis Block", "0")
        self.chain.append(genesis_block)
    
    def get_latest_block(self):
        """
        Get the last block in the chain.
        
        Returns:
            Block: The most recent block
        """
        return self.chain[-1]
    
    def add_block(self, data):
        """
        Add a new block to the blockchain.
        
        Args:
            data (str): Data to be stored in the new block
        """
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_timestamp = time()
        new_block = Block(new_index, new_timestamp, data, previous_block.hash)
        self.chain.append(new_block)
        print(f"Block #{new_index} added to the blockchain!")
    
    def is_chain_valid(self):
        """
        Check if the blockchain is valid by verifying hashes and links.
        
        Returns:
            bool: True if valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {i}")
                return False
            
            # Check if the current block points to the correct previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid link at block {i}")
                return False
        
        return True
    
    def display_chain(self):
        """Display all blocks in the blockchain."""
        print("\n" + "="*70)
        print("BLOCKCHAIN")
        print("="*70)
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"Timestamp: {datetime.fromtimestamp(block.timestamp)}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 70)
