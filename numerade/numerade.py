from numerade.finder_functions import fetch_page_source, extract_details, process_videos
from numerade.display import display_solution
from numerade.get_question import get_question

def run_numerade(url):
    if not "numerade.com" in url:
      print("The URL is not from numerade.com")
      return
    
    source_code = fetch_page_source(url)
    final_urls = extract_details(source_code)

    get_question(url)
    
    if final_urls:
        process_videos(final_urls)
    else:
        print("No video URLs found.")
