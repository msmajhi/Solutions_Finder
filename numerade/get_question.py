import requests
from bs4 import BeautifulSoup

def get_question(url):
    page_source = fetch_page_source(url)
    if page_source:
        pre_contents = find_pre_contents(page_source)
        write_to_file(pre_contents)
        # print("Contents of <pre> tags have been written to question.txt")

# Function to fetch the page source
def fetch_page_source(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

# Function to find the contents of <pre> tags
def find_pre_contents(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    pre_tags = soup.find_all('pre')
    return [tag.get_text() for tag in pre_tags]

# Function to write contents to question.txt
def write_to_file(contents):
    with open("question.txt", "w") as file:
        for content in contents:
            file.write(content + "\n")
