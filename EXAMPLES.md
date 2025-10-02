# Example Output

This document shows what you can expect when running the blockchain applications.

## Demo Script Output (demo.py)

```
======================================================================
WELCOME TO BASIC BLOCKCHAIN DEMO
======================================================================

1. Creating a new blockchain...
✓ Blockchain created with Genesis Block

2. Adding blocks to the blockchain...
Block #1 added to the blockchain!
Block #2 added to the blockchain!
Block #3 added to the blockchain!

3. Displaying the blockchain...

======================================================================
BLOCKCHAIN
======================================================================

Block #0
Timestamp: 2025-10-02 04:04:29.459562
Data: Genesis Block
Previous Hash: 0
Hash: 582b61ddc81a5d8a437a4502524f7a7ede6d93edc2d1cd292f08b4d442317f0c
----------------------------------------------------------------------

Block #1
Timestamp: 2025-10-02 04:04:29.459622
Data: First transaction: Alice sends 10 BTC to Bob
Previous Hash: 582b61ddc81a5d8a437a4502524f7a7ede6d93edc2d1cd292f08b4d442317f0c
Hash: 7dbe2641a1a07ad6b7ca8655bbe806371e11c1651039480818612dd53c14fcf4
----------------------------------------------------------------------

Block #2
Timestamp: 2025-10-02 04:04:29.459660
Data: Second transaction: Bob sends 5 BTC to Charlie
Previous Hash: 7dbe2641a1a07ad6b7ca8655bbe806371e11c1651039480818612dd53c14fcf4
Hash: 9bfa6b9b8dc83c9a36cdb13269644d5ca5cdec957a3b31cbb81babf7802c1d87
----------------------------------------------------------------------

Block #3
Timestamp: 2025-10-02 04:04:29.459689
Data: Third transaction: Charlie sends 2 BTC to David
Previous Hash: 9bfa6b9b8dc83c9a36cdb13269644d5ca5cdec957a3b31cbb81babf7802c1d87
Hash: 5dd92d543316b98a5b2fc182ba5a03ab1a1a69148189e84b443b77821afaeba5
----------------------------------------------------------------------

4. Validating the blockchain...
✓ Blockchain is valid!

5. Attempting to tamper with the blockchain...
   Changing data in Block #2...

6. Validating blockchain after tampering...
Invalid hash at block 2
✗ Blockchain is NOT valid! Tampering detected!

======================================================================
DEMO COMPLETED
======================================================================
```

## Interactive Application (interactive.py)

```
======================================================================
WELCOME TO INTERACTIVE BLOCKCHAIN APPLICATION
======================================================================
Initializing blockchain...
✓ Blockchain created successfully with Genesis Block!

======================================================================
BLOCKCHAIN APPLICATION - MENU
======================================================================
1. Add a new block
2. Display blockchain
3. Validate blockchain
4. Get blockchain info
5. Exit
======================================================================

Enter your choice (1-5): 1

Enter block data (transaction/message): Alice sends 50 BTC to Bob
Block #1 added to the blockchain!

======================================================================
BLOCKCHAIN APPLICATION - MENU
======================================================================
1. Add a new block
2. Display blockchain
3. Validate blockchain
4. Get blockchain info
5. Exit
======================================================================

Enter your choice (1-5): 4

======================================================================
BLOCKCHAIN INFORMATION
======================================================================
Total blocks: 2
Latest block index: 1
Latest block hash: ac82b56ccf4257ae2f2daa19983518fc1975826fc79a57b838ad9d981b69c754
======================================================================
```

## Using in Your Own Code

```python
from blockchain import Blockchain

# Create a new blockchain
my_blockchain = Blockchain()

# Add some blocks
my_blockchain.add_block("Alice pays Bob 10 BTC")
my_blockchain.add_block("Bob pays Charlie 5 BTC")
my_blockchain.add_block("Charlie pays Dave 2 BTC")

# Display the entire chain
my_blockchain.display_chain()

# Check if the blockchain is valid
if my_blockchain.is_chain_valid():
    print("✓ Blockchain is valid!")
else:
    print("✗ Blockchain has been tampered with!")

# Get the latest block
latest = my_blockchain.get_latest_block()
print(f"Latest block index: {latest.index}")
print(f"Latest block hash: {latest.hash}")

# Access individual blocks
for block in my_blockchain.chain:
    print(f"Block {block.index}: {block.data}")
```

## Key Observations

1. **Genesis Block**: Always block #0 with previous hash of "0"
2. **Hash Linking**: Each block's previous_hash matches the previous block's hash
3. **Timestamps**: Automatically added when blocks are created
4. **SHA-256**: Produces 64-character hexadecimal hashes
5. **Tampering Detection**: Any modification breaks the chain validation
6. **Immutability**: Once added, blocks should not be modified (blockchain principle)

## Understanding the Hashes

The hash is calculated from:
- Block index
- Timestamp
- Data
- Previous hash

If ANY of these change, the hash changes, breaking the chain!
