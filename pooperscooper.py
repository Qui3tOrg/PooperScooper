import requests
import random
import string
import os
import time

# Create a folder to store found files
found_folder = "FOUND"
if not os.path.exists(found_folder):
    os.makedirs(found_folder)

# URL bases
base_urls = ["https://files.catbox.moe/", "https://litter.catbox.moe/"]

# Supported file extensions
file_extensions = ["jpg", "png", "gif", "pdf"]

# Function to generate random filenames
def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Function to search for files indefinitely
def search_for_files():
    while True:
        filename = generate_random_filename()
        for base_url in base_urls:
            for extension in file_extensions:
                url = f"{base_url}{filename}.{extension}"
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        # File found, save it
                        file_path = os.path.join(found_folder, f"{filename}.{extension}")
                        with open(file_path, "wb") as f:
                            f.write(response.content)
                        print(f"Found and saved: {url}")
                    else:
                        print(f"Not found: {url}")
                except requests.RequestException as e:
                    print(f"Error accessing {url}: {e}")

                # Wait for 2 seconds before the next request
                time.sleep(2)

# Start searching for files indefinitely
search_for_files()
