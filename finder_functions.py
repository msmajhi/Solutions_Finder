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

def process_videos(video_urls):
    """
    Process the list of video URLs by checking if each URL contains a video.
    
    Args:
    video_urls (list): List of video URLs.
    """
    for url in video_urls:
        try:
            response = requests.head(url, allow_redirects=True)
            if response.headers.get('Content-Type', '').startswith('video'):
                print(f"Video found: {url}")
                
                content = f"""{repr(url)}"""
                # Write to final_video.py
                with open("Solutions_Finder/final_video.txt", "w") as file:
                  file.write(content)
            else:
                print(f"No video found at: {url}")
        except requests.RequestException as e:
            print(f"Error checking {url}: {e}")
