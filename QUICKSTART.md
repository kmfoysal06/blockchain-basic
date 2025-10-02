# Quick Start Guide

Welcome to the Basic Blockchain Application! This guide will get you started in less than 2 minutes.

## 🏃 Quick Start (3 Steps)

### Step 1: Verify Python Installation
```bash
python3 --version
```
or on Windows:
```bash
python --version
```

You need Python 3.6 or higher. If you don't have it, download from [python.org](https://www.python.org/downloads/).

### Step 2: Run the Demo
```bash
python3 demo.py
```
or on Windows:
```bash
python demo.py
```

This will automatically demonstrate all blockchain features!

### Step 3: Try the Interactive Mode
```bash
python3 interactive.py
```
or on Windows:
```bash
python interactive.py
```

Choose from the menu to:
- Add new blocks
- Display the blockchain
- Validate the chain
- Get blockchain information

## 📝 What You'll See

The demo will show you:
1. ✓ Creating a blockchain with a genesis block
2. ✓ Adding multiple blocks with transactions
3. ✓ Displaying all blocks with their hashes
4. ✓ Validating the blockchain integrity
5. ✓ Detecting tampering when data is modified

## 🎯 Next Steps

After running the demo and interactive mode:
1. Look at `blockchain.py` to understand the implementation
2. Try adding your own blocks with custom data
3. Experiment with the code in your own Python scripts
4. Read the full README.md for more details

## 💡 Example Usage in Your Code

```python
from blockchain import Blockchain

# Create blockchain
my_chain = Blockchain()

# Add blocks
my_chain.add_block("Alice pays Bob 10 BTC")
my_chain.add_block("Bob pays Charlie 5 BTC")

# Display and validate
my_chain.display_chain()
print("Valid:", my_chain.is_chain_valid())
```

## 🤔 Need Help?

If you encounter any issues:
1. Make sure Python 3.6+ is installed
2. Check that you're in the correct directory
3. Verify all files (blockchain.py, demo.py, interactive.py) are present
4. Try running `python3` instead of `python` (or vice versa)

Enjoy learning about blockchain technology! 🚀
