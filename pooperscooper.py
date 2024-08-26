import requests
import random
import string
import os
import time

# Log file to store found URLs
log_file = "FOUND.txt"

# URL bases
base_urls = ["https://files.catbox.moe/", "https://litter.catbox.moe/"]

# Supported file extensions
file_extensions = ["jpg", "jpeg", "bmp", "png", "svg", "tiff", "webp", "gif", "gifv", "webm", "mkv", "flv", "vob", "ogv", "ogg", "drc", "mng", "avi", "mts", "m2ts", "ts", "mov", "qt", "wmv", "yuv", "rm", "rmvb", "viv", "amv", "mp4", "m4p", "m4v", "mpg", "mp2", "mpeg", "mpe", "mpv", "m2v", "svi", "3gp", "3g2", "mxf", "roq", "nsv", "f4v", "f4p", "f4a", "f4b", "pdf", "zip", "rar", "tar", "tar.gz", "tgz", "tar.bz2", "tbz2", "tar.xz", "txz", "7z", "gz", "bz2", "xz", "lzma", "z", "cab"]

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
                        # File found, log it
                        with open(log_file, "a") as f:
                            f.write(f"{url}\n")
                        print(f"Found and logged: {url}")
                    else:
                        print(f"Not found: {url}")
                except requests.RequestException as e:
                    print(f"Error accessing {url}: {e}")

                # Wait for 2 seconds before the next request
                time.sleep(2)

# Start searching for files indefinitely
search_for_files()
