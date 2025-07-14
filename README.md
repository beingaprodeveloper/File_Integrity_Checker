# File Integrity Checker
                  About the Project
This is a **File Integrity Checker Tool** built using **Python**.  
It monitors changes in files by **calculating and comparing hash values**.  
It helps to detect if a file has been **changed, deleted, or added**.

## Features
    - Scan a folder and create hash records.
    - Check files for changes using SHA-256 hash.
    - Detect:
            - New files
            - Changed files
            - Deleted files

## How It Works (Step by Step)
       1️⃣ First Time Run (Create Hashes)
               - Run the script.
               - Enter the folder path you want to scan.
               - The tool will create a file called `hashes.json` to save the file hashes.

### 2️⃣ Second Time Run (Check for Changes)
              - Run the script again on the **same folder**.
              - The tool will compare current file hashes with `hashes.json`.
              - It will show:
                             - `[CHANGED]` – If a file is modified.
                             - `[NEW]` – If a new file is added.
                             - `[DELETED]` – If a file is missing.

## Requirements
              - Python 3.x  
              - Libraries used: `hashlib`, `os`, `json`

## How to Run
              ### Windows
```bash
python file_integrity_checker.py


