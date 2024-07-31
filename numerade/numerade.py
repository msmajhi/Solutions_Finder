from finder_functions import fetch_page_source, extract_details, process_videos
from display import display_solution

def run_numerade(url):
    if not "numerade.com" in url:
      print("The URL is not from numerade.com")
      return
    
    source_code = fetch_page_source(url)
    final_urls = extract_details(source_code)
    
    if final_urls:
        process_videos(final_urls)
    else:
        print("No video URLs found.")

    display_solution()
