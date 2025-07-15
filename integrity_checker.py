import os
import hashlib
import json

HASH_FILE = 'hashes.json'
TARGET_DIR = 'monitored_files'

def calculate_hash(filepath):
    """Calculate SHA-256 hash of a file"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def scan_and_store_hashes():
    """Scan files and store their hashes"""
    file_hashes = {}
    for root, _, files in os.walk(TARGET_DIR):
        for filename in files:
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, TARGET_DIR)
            file_hashes[rel_path] = calculate_hash(full_path)
    
    with open(HASH_FILE, 'w') as f:
        json.dump(file_hashes, f, indent=4)
    
    print("Initial hashes stored successfully.")

def check_file_integrity():
    """Check current file hashes against stored ones"""
    try:
        with open(HASH_FILE, 'r') as f:
            stored_hashes = json.load(f)
    except FileNotFoundError:
        print("Hash file not found. Please run initial scan first.")
        return

    changed_files = []
    for rel_path, original_hash in stored_hashes.items():
        full_path = os.path.join(TARGET_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"[MISSING] {rel_path} has been deleted or moved.")
            continue
        
        current_hash = calculate_hash(full_path)
        if current_hash != original_hash:
            changed_files.append(rel_path)
            print(f"[MODIFIED] {rel_path}")

    if not changed_files:
        print("All files are intact. No changes detected.")
    else:
        print(f"{len(changed_files)} file(s) modified.")

def menu():
    """CLI Menu"""
    while True:
        print("\n📦 File Integrity Checker")
        print("1. Run initial hash scan")
        print("2. Check file integrity")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            scan_and_store_hashes()
        elif choice == '2':
            check_file_integrity()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
