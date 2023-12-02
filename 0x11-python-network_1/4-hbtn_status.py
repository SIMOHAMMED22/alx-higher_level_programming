#!/usr/bin/python3
"""Python script that fetches
https://alx-intranet.hbtn.io/status"""


import urllib.request
import urllib.error
import sys

def fetch_url_body(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_url_body(url)
    else:
        print("Error: Please provide a URL as an argument.")
