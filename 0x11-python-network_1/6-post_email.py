#!/usr/bin/python3
"""sends a POST request to the passed
URL with the email as a parameter"""


import requests
import sys


def send_post_request(url, email):
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
