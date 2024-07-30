import requests

def get_url():
    url = input("Enter a URL from site 'numerade.com': ")
    if "numerade.com" not in url:
        print("The URL is not from this site.")
        return None
    return url

def fetch_and_save_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        source_code = response.text

        with open("details.txt", "w") as file:
            for line in source_code.splitlines():
                if "videoUrl" in line or "bucketFolder" in line:
                    file.write(line + "\n")
        print("Details saved to 'details.txt'.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = get_url()
    if url:
        fetch_and_save_details(url)
