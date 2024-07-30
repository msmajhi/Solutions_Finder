from finder_functions import fetch_page_source, extract_details, process_videos

def main():
    url = input("Enter a URL from site 'numerade.com': ")
    
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
    main()
