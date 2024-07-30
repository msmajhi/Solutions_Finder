import requests
import re
import os
import time  # Import the time module
from urllib.parse import urlparse

def fetch_page_source(url, retries=10, delay=5):
    """Fetch the source code of the given URL with retry logic."""
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)  # Wait before retrying
    print("All retry attempts failed.")
    return ""

def extract_details(source_code):
    """Extract videoUrl and bucketFolder values and construct final URLs."""
    video_urls = []
    bucket_folders = []

    # Regular expressions to match videoUrl and bucketFolder
    video_url_pattern = re.compile(r'videoUrl\s*=\s*"([^"]+)"')
    bucket_folder_pattern = re.compile(r'bucketFolder\s*=\s*"([^"]+)"')

    video_urls = video_url_pattern.findall(source_code)
    bucket_folders = bucket_folder_pattern.findall(source_code)

    final_urls = []
    for video_url, bucket_folder in zip(video_urls, bucket_folders):
        final_url = f"https://cdn.numerade.com/{bucket_folder}/{video_url}.mp4"
        final_urls.append(final_url)

    return final_urls

def download_video(url, folder="Solutions"):
    """Download video from URL and save it with an incrementing filename."""
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Determine the file extension
        content_type = response.headers.get('Content-Type')
        extension = content_type.split('/')[1] if content_type else 'mp4'

        # Determine the filename
        base_filename = os.path.join(folder, f"solution_1.{extension}")
        counter = 1
        while os.path.exists(base_filename):
            counter += 1
            base_filename = os.path.join(folder, f"solution_{counter}.{extension}")

        # Save the video
        with open(base_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded and saved video as {base_filename}.")
    except requests.RequestException as e:
        print(f"Failed to download video from {url}: {e}")

def process_videos(urls):
    """Process the list of URLs to download videos."""
    for url in urls:
        download_video(url)
