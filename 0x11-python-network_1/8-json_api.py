#!/usr/bin/python3
"""sends a POST request ,query"""


import requests
import sys


def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}

    try:
        response = requests.post(url, params=params)
        json_data = response.json()

        if json_data:
            if 'id' in json_data and 'name' in json_data:
                print(f"[{json_data['id']}] {json_data['name']}")
            else:
                print("Not a valid JSON")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
    except requests.RequestException as e:
        print(f"Request Error: {e}")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
