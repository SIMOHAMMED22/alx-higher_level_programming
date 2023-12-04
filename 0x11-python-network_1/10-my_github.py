#!/usr/bin/python3
"""Using the GitHub API to get my User Id"""


import requests
import sys


def display_user_id(username, password):
    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            print(f"Your GitHub user ID is: {user_data['id']}")
        else:
            print(f"Failed to retrieve user data. Status code:
                {response.status_code}")
    except requests.RequestException as e:
        print(f"Request Error: {e}")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    display_user_id(username, password)
