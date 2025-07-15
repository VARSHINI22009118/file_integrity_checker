# 🔐 File Integrity Checker

## Aim:
To develop a Python-based file integrity checker that calculates and stores cryptographic hashes of monitored files, enabling detection of unauthorized modifications by comparing current file states with previously stored hash values—thus simulating how security systems detect tampering or malware infections.

## 🧠 What It Does

This Python-based CLI tool helps detect unauthorized file modifications. It:
Calculates a SHA-256 hash of each file in a monitored folder.
Saves the original hashes in a hashes.json file.
Re-checks those files later to detect any tampering.
Alerts if any file was modified or deleted.
This simulates how antivirus and endpoint security tools verify file integrity.

## 🎯 Use Case / Goal

✅ Demonstrates how security software detects malicious changes to:
System files
Configuration files
Scripts and sensitive documents

✅ Helps learn:
Cryptographic hashing (SHA-256)
Python file I/O
CLI interface and integrity validation

## 🧰 Requirements
```

Tool	              Purpose
hashlib    -    Generate file hashes (SHA-256)
os         -    Traverse file directories
json	   -    Store and retrieve hash data

```

✅ No external libraries required — just core Python (3.6+).

## 📁 Project Structure

```
file_integrity_checker/
├── integrity_checker.py      # Main Python script
├── monitored_files/          # Folder with files to monitor
└── hashes.json               # Auto-generated file storing original hashes

```
## 💻 How It Works
  
1️⃣ User runs integrity_checker.py
2️⃣ A CLI menu appears:
    - Option 1: Run initial hash scan
    - Option 2: Check file integrity
3️⃣ Hashes of files in monitored_files/ are calculated
4️⃣ Results are stored (or compared) in hashes.json

### If files are modified, you'll see:

```
[MODIFIED] notes.txt
1 file(s) modified.

```
### If everything is fine:
```
All files are intact. No changes detected.
```

## 🔢 Program

### 🧩 calculate_hash() Function
```
def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()
```

### 🧩 check_file_integrity() Function
```
def check_file_integrity():
    with open(HASH_FILE, 'r') as f:
        stored_hashes = json.load(f)

    for rel_path, original_hash in stored_hashes.items():
        full_path = os.path.join(TARGET_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"[MISSING] {rel_path}")
        elif calculate_hash(full_path) != original_hash:
            print(f"[MODIFIED] {rel_path}")
```

## Complete code snippet
### integrity_checker.py

```
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

```


## 🛠️ How to Run This in VS Code
Create Folder


mkdir file_integrity_checker
cd file_integrity_checker
Create Script

Add integrity_checker.py and paste the full code.

Create a folder called monitored_files/

Add test files like notes.txt, config.json, etc.

Run Script
```
python integrity_checker.py
```

### 🧾 Sample Output

✅ Initial Scan:

📦 File Integrity Checker
1. Run initial hash scan
2. Check file integrity
3. Exit
Choose an option: 1
Initial hashes stored successfully.


⚠️ After Modifying a File:

📦 File Integrity Checker
1. Run initial hash scan
2. Check file integrity
3. Exit
Choose an option: 2
```
[MODIFIED] notes.txt
1 file(s) modified.
```
<img width="1123" height="326" alt="image" src="https://github.com/user-attachments/assets/1d84aafe-c1f6-42b2-a0b6-ef877b2b1ee3" />


## 🔐 Why This Is Useful in Cybersecurity
✅ Demonstrates how hashing can detect unauthorized tampering
✅ Mimics antivirus behavior for integrity checks
✅ Can evolve into a real-time monitor or automated watchdog

## 💡 Extension Ideas
🔔 Send email alerts on file changes
🖥️ Add a GUI using Tkinter
🧪 Compare multiple hash types (SHA-1, MD5, etc.)
🔄 Auto-backup modified files
🕓 Run as a scheduled task (cron job / Windows Task Scheduler)

## Result:
A robust Python-based command-line tool was successfully developed to monitor file integrity by calculating and comparing SHA-256 hashes, effectively detecting any unauthorized modifications, deletions, or tampering of files within a specified directory.












