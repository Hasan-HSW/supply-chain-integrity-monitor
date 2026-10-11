from datetime import datetime

# Define the historical log file destination
LOG_FILE = "scan_log.txt"


def log_scan_results(results: list) -> None:
    """
    Appends detailed results of every verification run into scan_log.txt for auditing.

    Parameters:
        results (list): List of dictionaries containing file scan details.
    """
    # Get current timestamp formatted as YYYY-MM-DD HH:MM:SS
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open log file in Append mode ("a") so past historical scans are preserved
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n=== Scan Session Timestamp: {timestamp} ===\n")

        for res in results:
            # Map boolean status to human-readable string
            status_str = "SAFE" if res["status"] else "WARNING (Possible Supply Chain Tampering)"

            # Format and write individual file audit records
            f.write(f"File Path:    {res['file_path']}\n")
            f.write(f"Scan Status:  {status_str}\n")
            f.write(f"Trusted Hash: {res['stored_hash']}\n")
            f.write(f"Current Hash: {res['current_hash']}\n")
            f.write("-" * 50 + "\n")


def view_logs() -> None:
    """
    Reads and prints all historical log contents from scan_log.txt to console screen.
    """
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            print("\n" + f.read())
    except FileNotFoundError:
        print("\n[!] No previous log records found. Run a verification scan first.")