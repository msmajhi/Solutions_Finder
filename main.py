"""
Run this as - $ python main.py "{question url}"
"""

import argparse
from numerade.numerade import run_numerade

def main(url, site):
    if site == "numerade.com":
      run_numerade(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a URL')
    parser.add_argument('url', type=str, help='The URL to process')
    parser.add_argument('site', type=str, help='The site')
    args = parser.parse_args()
      
    main(args.url, args.site)
