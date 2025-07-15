🔐 File Integrity Checker
🧠 What It Does
This Python-based CLI tool helps detect unauthorized file modifications. It:

Calculates a SHA-256 hash of each file in a monitored folder.

Saves the original hashes in a hashes.json file.

Re-checks those files later to detect any tampering.

Alerts if any file was modified or deleted.

This simulates how antivirus and endpoint security tools verify file integrity.

🎯 Use Case / Goal
✅ Demonstrates how security software detects malicious changes to:

System files

Configuration files

Scripts and sensitive documents

✅ Helps learn:

Cryptographic hashing (SHA-256)

Python file I/O

CLI interface and integrity validation

🧰 Requirements
Tool	Purpose
hashlib	Generate file hashes (SHA-256)
os	Traverse file directories
json	Store and retrieve hash data

✅ No external libraries required — just core Python (3.6+).

📁 Project Structure
bash
Copy
Edit
file_integrity_checker/
├── integrity_checker.py      # Main Python script
├── monitored_files/          # Folder with files to monitor
└── hashes.json               # Auto-generated file storing original hashes
💻 How It Works
python
Copy
Edit
1️⃣ User runs integrity_checker.py
2️⃣ A CLI menu appears:
    - Option 1: Run initial hash scan
    - Option 2: Check file integrity
3️⃣ Hashes of files in monitored_files/ are calculated
4️⃣ Results are stored (or compared) in hashes.json
If files are modified, you'll see:

scss
Copy
Edit
[MODIFIED] notes.txt
1 file(s) modified.
If everything is fine:

sql
Copy
Edit
All files are intact. No changes detected.
🔢 Sample Code Snippet
🧩 calculate_hash() Function
python
Copy
Edit
def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()
🧩 check_file_integrity() Function
python
Copy
Edit
def check_file_integrity():
    with open(HASH_FILE, 'r') as f:
        stored_hashes = json.load(f)

    for rel_path, original_hash in stored_hashes.items():
        full_path = os.path.join(TARGET_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"[MISSING] {rel_path}")
        elif calculate_hash(full_path) != original_hash:
            print(f"[MODIFIED] {rel_path}")
🛠️ How to Run This in VS Code
Create Folder

bash
Copy
Edit
mkdir file_integrity_checker
cd file_integrity_checker
Create Script

Add integrity_checker.py and paste the full code.

Create a folder called monitored_files/

Add test files like notes.txt, config.json, etc.

Run Script

bash
Copy
Edit
python3 integrity_checker.py
🧾 Sample Output
✅ Initial Scan:
mathematica
Copy
Edit
📦 File Integrity Checker
1. Run initial hash scan
2. Check file integrity
3. Exit
Choose an option: 1
Initial hashes stored successfully.
⚠️ After Modifying a File:
mathematica
Copy
Edit
📦 File Integrity Checker
1. Run initial hash scan
2. Check file integrity
3. Exit
Choose an option: 2
[MODIFIED] notes.txt
1 file(s) modified.
🔐 Why This Is Useful in Cybersecurity
✅ Demonstrates how hashing can detect unauthorized tampering
✅ Mimics antivirus behavior for integrity checks
✅ Can evolve into a real-time monitor or automated watchdog

💡 Extension Ideas
🔔 Send email alerts on file changes

🖥️ Add a GUI using Tkinter

🧪 Compare multiple hash types (SHA-1, MD5, etc.)

🔄 Auto-backup modified files

🕓 Run as a scheduled task (cron job / Windows Task Scheduler)


