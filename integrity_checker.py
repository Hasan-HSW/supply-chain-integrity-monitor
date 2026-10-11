import os
from hash_utils import calculate_sha256, compare_hashes
from file_manager import load_trusted_hashes

# ANSI escape codes for coloring output text in standard terminals
GREEN = "\033[92m"  # Used for SAFE status
RED = "\033[91m"  # Used for WARNING status
RESET = "\033[0m"  # Resets text color back to default


def verify_all_files() -> list:
    """
    Core Defensive Engine:
    Iterates through all registered files, recalculates their live SHA-256 hashes,
    and compares them against stored trusted hashes to detect unauthorized tampering.
    """
    # Fetch all previously registered files and hashes from JSON storage
    trusted_hashes = load_trusted_hashes()

    if not trusted_hashes:
        print("\n[!] No files registered for verification yet. Please register files first.")
        return []

    results = []
    print("\n--- Starting Integrity Verification Scan ---")

    # Iterate over every registered file path and its known trusted hash
    for file_path, stored_hash in trusted_hashes.items():
        # Edge Case: Check if the file was deleted or moved from its location
        if not os.path.isfile(file_path):
            print(f"\n[!] Missing File Error: {file_path}")
            current_hash = "FILE_MISSING"
            is_safe = False
        else:
            # Recalculate live SHA-256 hash of file on disk
            current_hash = calculate_sha256(file_path)
            # Compare stored trusted hash with the live calculated hash
            is_safe = compare_hashes(stored_hash, current_hash)

        # Store scan information into dictionary
        results.append({
            "file_path": file_path,
            "stored_hash": stored_hash,
            "current_hash": current_hash,
            "status": is_safe
        })

        # Display formatted report to console screen
        print(f"\nFile: {os.path.basename(file_path)}")
        print(f"Trusted Hash: {stored_hash}")
        print(f"Current Hash: {current_hash}")

        # Render status alert based on integrity check
        if is_safe:
            print(f"Status: {GREEN}SAFE{RESET}")
        else:
            print(f"Status: {RED}WARNING{RESET}")
            print(f"{RED}Possible Supply Chain Attack Detected! The file integrity has been compromised.{RESET}")

    return results