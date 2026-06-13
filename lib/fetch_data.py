import requests

def fetch_data():
    """Fetch a post from a public API."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def save_to_file(data):
    """Write fetched data to a text file."""
    with open("fetched_post.txt", "w") as file:
        file.write(f"Title: {data.get('title', 'No title found')}\n")
        file.write(f"Body: {data.get('body', 'No body found')}\n")
        file.write(f"User ID: {data.get('userId', 'Unknown')}\n")
    print("Data saved to fetched_post.txt")

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    save_to_file(post)