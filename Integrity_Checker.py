import os
import hashlib
import json

HASH_FILE = "hashes.json"

def calculate_hash(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"[ERROR] Unable to hash {filepath}: {e}")
        return None

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = calculate_hash(full_path)
            if file_hash:
                file_hashes[full_path] = file_hash
    return file_hashes

def load_previous_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, 'w') as f:
        json.dump(hashes, f, indent=2)

def compare_hashes(old, new):
    print("\n--- File Integrity Check ---\n")
    all_files = set(old) | set(new)

    for file in all_files:
        if file not in old:
            print(f"[NEW]      {file}")
        elif file not in new:
            print(f"[DELETED]  {file}")
        elif old[file] != new[file]:
            print(f"[CHANGED]  {file}")
        else:
            print(f"[UNCHANGED] {file}")

def main():
    directory = input("Enter directory to scan: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    old_hashes = load_previous_hashes()
    new_hashes = scan_directory(directory)
    compare_hashes(old_hashes, new_hashes)
    save_hashes(new_hashes)
    print("\nHash comparison complete. Ready for next run.\n")

if __name__ == "__main__":
    main()
