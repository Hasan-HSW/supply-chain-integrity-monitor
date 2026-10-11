import json
import os
from typing import Dict
from hash_utils import calculate_sha256

# Define the local database file path where trusted file paths and hashes are stored
DB_FILE = "trusted_hashes.json"


def load_trusted_hashes() -> Dict[str, str]:
    """
    Loads the database of previously saved trusted hashes from the JSON file.

    Returns:
        A dictionary where:
        - Key: Absolute file path (e.g., "C:/projects/clean.txt")
        - Value: Stored SHA-256 hash
    """
    # If database file does not exist yet, return an empty dictionary
    if not os.path.exists(DB_FILE):
        return {}

    try:
        # Read and parse JSON content into a Python dictionary
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[!] Error loading trusted hashes database: {e}")
        return {}


def save_trusted_hashes(hashes: Dict[str, str]) -> None:
    """
    Saves/Updates the dictionary of trusted file paths and hashes into the JSON database.
    """
    # Write dictionary back to JSON file formatted with 4 spaces indent for readability
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=4)


def register_file(file_path: str) -> bool:
    """
    Registers a file into the trusted database.

    Steps:
    1. Validates file existence.
    2. Converts relative path to absolute path to prevent ambiguity.
    3. Calculates current SHA-256 hash.
    4. Saves path and hash pair into trusted_hashes.json.
    """
    # Step 1: Ensure path points to a valid existing file
    if not os.path.isfile(file_path):
        print("\n[!] Error: Invalid file path or file does not exist.")
        return False

    # Step 2: Convert path to absolute path (e.g., C:/Users/.../sample.txt)
    abs_path = os.path.abspath(file_path)

    # Step 3: Compute current SHA-256 hash of the file
    current_hash = calculate_sha256(abs_path)

    # Step 4: Load existing database, add/update current file record, and write to disk
    trusted_hashes = load_trusted_hashes()
    trusted_hashes[abs_path] = current_hash
    save_trusted_hashes(trusted_hashes)

    print(f"\n[+] File registered successfully into trusted database:")
    print(f"    Path: {abs_path}")
    print(f"    SHA-256: {current_hash}")
    return True