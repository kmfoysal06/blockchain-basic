#!/usr/bin/env python3
"""
Interactive Blockchain Application
This script allows users to interact with the blockchain through a menu.
"""

from blockchain import Blockchain


def print_menu():
    """Display the main menu."""
    print("\n" + "="*70)
    print("BLOCKCHAIN APPLICATION - MENU")
    print("="*70)
    print("1. Add a new block")
    print("2. Display blockchain")
    print("3. Validate blockchain")
    print("4. Get blockchain info")
    print("5. Exit")
    print("="*70)


def get_blockchain_info(blockchain):
    """Display information about the blockchain."""
    print("\n" + "="*70)
    print("BLOCKCHAIN INFORMATION")
    print("="*70)
    print(f"Total blocks: {len(blockchain.chain)}")
    print(f"Latest block index: {blockchain.get_latest_block().index}")
    print(f"Latest block hash: {blockchain.get_latest_block().hash}")
    print("="*70)


def main():
    print("="*70)
    print("WELCOME TO INTERACTIVE BLOCKCHAIN APPLICATION")
    print("="*70)
    print("Initializing blockchain...")
    
    # Create a new blockchain
    blockchain = Blockchain()
    print("✓ Blockchain created successfully with Genesis Block!\n")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            data = input("\nEnter block data (transaction/message): ").strip()
            if data:
                blockchain.add_block(data)
            else:
                print("Error: Block data cannot be empty!")
        
        elif choice == "2":
            blockchain.display_chain()
        
        elif choice == "3":
            print("\nValidating blockchain...")
            if blockchain.is_chain_valid():
                print("✓ Blockchain is valid!")
            else:
                print("✗ Blockchain is NOT valid!")
        
        elif choice == "4":
            get_blockchain_info(blockchain)
        
        elif choice == "5":
            print("\nThank you for using the Blockchain Application!")
            print("Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
