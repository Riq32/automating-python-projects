from datetime import datetime


def generate_log(log_data):
    """Write the list of log entries to a dated log file and return filename.

    Args:
        log_data (list): List of strings to write as log lines.

    Returns:
        str: The filename written (e.g. "log_YYYYMMDD.txt").

    Raises:
        ValueError: If `log_data` is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename