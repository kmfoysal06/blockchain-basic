#!/usr/bin/env python3
"""
Blockchain Demo Script
This script demonstrates the basic functionality of the blockchain.
"""

from blockchain import Blockchain


def main():
    print("="*70)
    print("WELCOME TO BASIC BLOCKCHAIN DEMO")
    print("="*70)
    
    # Create a new blockchain
    print("\n1. Creating a new blockchain...")
    my_blockchain = Blockchain()
    print("✓ Blockchain created with Genesis Block")
    
    # Add some blocks
    print("\n2. Adding blocks to the blockchain...")
    my_blockchain.add_block("First transaction: Alice sends 10 BTC to Bob")
    my_blockchain.add_block("Second transaction: Bob sends 5 BTC to Charlie")
    my_blockchain.add_block("Third transaction: Charlie sends 2 BTC to David")
    
    # Display the blockchain
    print("\n3. Displaying the blockchain...")
    my_blockchain.display_chain()
    
    # Validate the blockchain
    print("\n4. Validating the blockchain...")
    if my_blockchain.is_chain_valid():
        print("✓ Blockchain is valid!")
    else:
        print("✗ Blockchain is NOT valid!")
    
    # Demonstrate tampering detection
    print("\n5. Attempting to tamper with the blockchain...")
    print("   Changing data in Block #2...")
    my_blockchain.chain[2].data = "Tampered transaction: Bob sends 100 BTC to Charlie"
    
    print("\n6. Validating blockchain after tampering...")
    if my_blockchain.is_chain_valid():
        print("✓ Blockchain is valid!")
    else:
        print("✗ Blockchain is NOT valid! Tampering detected!")
    
    print("\n" + "="*70)
    print("DEMO COMPLETED")
    print("="*70)


if __name__ == "__main__":
    main()
