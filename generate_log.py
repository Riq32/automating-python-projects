from datetime import datetime

def generate_log(log_data):
    """
    Generate a log file with provided entries.
    
    log_data: list of log entries to write
    Returns the filename written to.
    Raises ValueError if log_data is not a list.
    """
    # Validate input - must be a list
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # Create filename with today's date e.g. log_20260608.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each entry to the file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename

if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)