"""
Run this as - $ python main.py "{question url}"
"""

import argparse
from finder_functions import fetch_page_source, extract_details, process_videos
from display import display_video
def main(url):
    if not "numerade.com" in url:
      print("The URL is not from this site.")
      return
    
    source_code = fetch_page_source(url)
    final_urls = extract_details(source_code)
    
    if final_urls:
        process_videos(final_urls)
    else:
        print("No video URLs found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a URL from numerade.com.')
    parser.add_argument('url', type=str, help='The URL to process')
    args = parser.parse_args()
      
    main(args.url)
