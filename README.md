# blockchain-basic

A simple and educational blockchain implementation in Python to understand the core concepts of blockchain technology.

> **🚀 Want to get started quickly?** Check out [QUICKSTART.md](QUICKSTART.md) for a 2-minute guide!
> 
> **📖 Want to see example outputs?** Check out [EXAMPLES.md](EXAMPLES.md) for detailed examples!

## 📋 Overview

This project implements a basic blockchain with the following features:
- Block creation with hash generation using SHA-256
- Blockchain validation
- Tamper detection
- Interactive and demo modes

## 🏗️ Structure

The project consists of three main files:

1. **blockchain.py** - Core blockchain implementation
   - `Block` class: Represents individual blocks
   - `Blockchain` class: Manages the chain of blocks

2. **demo.py** - Automated demonstration script
   - Shows how blocks are added
   - Demonstrates validation
   - Shows tamper detection

3. **interactive.py** - Interactive application
   - Menu-driven interface
   - Allows users to manually add blocks
   - Real-time validation

## 🚀 How to Run

### Prerequisites

- Python 3.6 or higher (Python comes with built-in libraries needed for this project)

### Running the Demo Script

The demo script automatically demonstrates blockchain functionality:

```bash
python3 demo.py
```

or on Windows:

```bash
python demo.py
```

### Running the Interactive Application

For hands-on experience with the blockchain:

```bash
python3 interactive.py
```

or on Windows:

```bash
python interactive.py
```

### Using the Blockchain in Your Code

You can also import and use the blockchain in your own Python scripts:

```python
from blockchain import Blockchain

# Create a new blockchain
my_chain = Blockchain()

# Add blocks
my_chain.add_block("Transaction 1: Alice pays Bob 10 BTC")
my_chain.add_block("Transaction 2: Bob pays Charlie 5 BTC")

# Display the chain
my_chain.display_chain()

# Validate the chain
if my_chain.is_chain_valid():
    print("Blockchain is valid!")
```

## 📖 Understanding the Code

### Block Structure

Each block contains:
- **Index**: Position in the blockchain
- **Timestamp**: When the block was created
- **Data**: Information stored in the block (e.g., transactions)
- **Previous Hash**: Hash of the previous block (links blocks together)
- **Hash**: Unique identifier calculated from all block data

### How It Works

1. **Genesis Block**: The first block is automatically created when you initialize a blockchain
2. **Adding Blocks**: New blocks are linked to previous blocks using cryptographic hashes
3. **Validation**: The blockchain validates by:
   - Checking each block's hash is correct
   - Verifying each block links to the previous block properly
4. **Tamper Detection**: If any data is modified, the hash changes and validation fails

## 🔍 Example Output

When you run the demo, you'll see:

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
Timestamp: 2024-01-01 12:00:00.123456
Data: Genesis Block
Previous Hash: 0
Hash: a1b2c3d4e5f6...
----------------------------------------------------------------------

Block #1
Timestamp: 2024-01-01 12:00:05.789012
Data: First transaction: Alice sends 10 BTC to Bob
Previous Hash: a1b2c3d4e5f6...
Hash: f6e5d4c3b2a1...
----------------------------------------------------------------------
...
```

## 🧪 Testing

To test the blockchain manually:

1. Run the interactive application
2. Add several blocks
3. Display the blockchain to see all blocks
4. Validate the blockchain (should be valid)

## 📚 Learning Resources

This is a basic implementation for educational purposes. Real-world blockchains include:
- Proof of Work / Proof of Stake consensus mechanisms
- Peer-to-peer networking
- Transaction pools
- Mining rewards
- Smart contracts (in some blockchains)

## 🤝 Contributing

Feel free to fork this project and experiment with:
- Adding proof-of-work (mining)
- Implementing a difficulty level
- Adding a transaction pool
- Creating a simple wallet system

## 📄 License

This project is open source and available for educational purposes.