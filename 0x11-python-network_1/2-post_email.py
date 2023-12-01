#!/usr/bin/python3
"""
Sends a POST request to the specified
URL with the email as a parameter,
and displays the body of the response.
"""


import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
