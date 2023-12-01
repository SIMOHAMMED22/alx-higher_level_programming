#!/usr/bin/python3
"""Sends a request to the URL and
displays the body of the response"""


import urllib.request
import urllib.error
import sys

if len(sys.argv) < 2:
    print("Please provide a URL.")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
