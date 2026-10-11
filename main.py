import os
from file_manager import register_file, load_trusted_hashes
from integrity_checker import verify_all_files
from logger import log_scan_results, view_logs

def display_menu():
    """
    Displays the interactive Command-Line Interface (CLI) menu.
    """
    print("\n==========================================")
    print(" Supply Chain Integrity Monitor (SHA-256) ")
    print("==========================================")
    print("1 Register File")
    print("2 Verify Files")
    print("3 Show Trusted Files")
    print("4 View Scan Log")
    print("5 Exit")
    print("==========================================")

def main():
    """
    Program Entry Point & Main Application Loop.
    """
    # Setup test environment: Automatically create 'sample_files/' folder and dummy files for demo
    sample_dir = "sample_files"
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)
        # Create a clean target file
        with open(os.path.join(sample_dir, "clean.txt"), "w") as f:
            f.write("Original untampered code base.")
        # Create a sample file intended to be modified during demo
        with open(os.path.join(sample_dir, "modified.txt"), "w") as f:
            f.write("Original code base.")

    # Main infinite loop to keep CLI menu running until user exits (Option 5)
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            # Feature 1: Register a file into trusted database
            filepath = input("Enter the path of the file to register (e.g., sample_files/clean.txt): ").strip()
            register_file(filepath)

        elif choice == "2":
            # Feature 2: Execute verification scan and log output
            results = verify_all_files()
            if results:
                log_scan_results(results)
                print("\n[+] Scan results appended to scan_log.txt")

        elif choice == "3":
            # Feature 3: Print currently tracked files in JSON DB
            trusted = load_trusted_hashes()
            if not trusted:
                print("\n[!] No registered files found in database.")
            else:
                print("\n--- Currently Registered Trusted Files ---")
                for path, h in trusted.items():
                    print(f"• File: {path}\n  SHA-256: {h}\n")

        elif choice == "4":
            # Feature 4: Display audit log history
            view_logs()

        elif choice == "5":
            # Feature 5: Terminate program
            print("\nExiting program. Goodbye!")
            break

        else:
            # Handle invalid input selections
            print("\n[!] Invalid option selected, please select 1-5.")

if __name__ == "__main__":
    # Ensure script executes only when run directly (not when imported as a module)
    main()