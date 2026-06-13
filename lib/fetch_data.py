#!/usr/bin/env python3
"""
fetch_data.py — Fetches a post from a public API and writes it to a file.
Requires: requests  (pip install requests)
"""

import requests
import json
from datetime import datetime


def fetch_data(url: str = "https://jsonplaceholder.typicode.com/posts/1") -> dict:
    """Fetch JSON data from a public API endpoint."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}


def save_to_file(data: dict, filename: str = None) -> str:
    """Write the fetched data to a .txt output file."""
    if filename is None:
        filename = f"api_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("=== API Fetch Result ===\n")
        file.write(f"Fetched at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

    print(f"Result saved to {filename}")
    return filename


if __name__ == "__main__":
    print("Fetching data from API...")
    post = fetch_data()

    if post:
        print(f"Fetched Post Title: {post.get('title', 'No title found')}")
        save_to_file(post)
    else:
        print("Failed to fetch data.")