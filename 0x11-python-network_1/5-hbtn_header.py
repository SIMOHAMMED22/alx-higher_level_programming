#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the value of the variable"""


import requests
import sys


def get_request_id(url):
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(f"X-Request-Id: {request_id}")
        else:
            print("X-Request-Id not found in the response headers.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    get_request_id(url)
