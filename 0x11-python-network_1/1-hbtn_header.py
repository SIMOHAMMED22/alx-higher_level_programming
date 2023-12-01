#!/usr/bin/python3
"""This script fetches a URL using urllib and sys,
 then displays the value of the X-Request-Id
 variable found in the header of the response."""


import urllib.request
import sys

url = sys.argv[1]

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
