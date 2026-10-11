import hashlib
import os


def calculate_sha256(file_path: str) -> str:
    """
    Calculates and returns the SHA-256 cryptographic hash of a given file.

    Why SHA-256?
    - SHA-256 produces a unique 64-character hexadecimal signature (hash) for any file content.
    - Even a tiny change (e.g., adding a single space) drastically changes the hash.

    Why Chunk-based Reading?
    - Instead of loading the entire file into RAM (which crashes for large files),
      we read it in small 4KB chunks iteratively.
    """
    # Verify that the path provided exists and points to an actual file
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Initialize the SHA-256 hashing object from Python's standard 'hashlib'
    sha256_hash = hashlib.sha256()

    # Open the file in Binary Read mode ("rb") to prevent text-encoding alterations
    with open(file_path, "rb") as f:
        # Read the file in 4096-byte (4KB) chunks until the end of the file (empty byte string b"")
        for byte_block in iter(lambda: f.read(4096), b""):
            # Update the hash object with the current block of bytes
            sha256_hash.update(byte_block)

    # Return the final calculated hash as a human-readable hexadecimal string
    return sha256_hash.hexdigest()


def compare_hashes(hash1: str, hash2: str) -> bool:
    """
    Compares two hash strings to check if they are identical.

    - Normalizes both strings to lowercase to avoid case-sensitivity issues.
    - Returns True if hashes match (file is unchanged/safe).
    - Returns False if hashes differ (file has been modified/tampered).
    """
    return hash1.lower() == hash2.lower()