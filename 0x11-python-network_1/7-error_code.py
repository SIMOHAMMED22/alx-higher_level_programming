#!/usr/bin/python3
"""sends a request to the URL and
displays the body of the response."""


import requests
import sys


def fetch_url_content(url):
    try:
        response = requests.get(url)
        print("Response body:")
        print(response.text)

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to fetch URL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_content(url)
