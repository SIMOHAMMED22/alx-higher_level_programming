#!/usr/bin/python3
"""Using the GitHub API to get commits from a repository"""

import requests
import sys


def get_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            commits = response.json()[:10]
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(f"Failed to retrieve commits. Status code: "
                  f"{response.status_code}")
    except requests.RequestException as e:
        print(f"Request Error: {e}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_commits(repo_name, owner_name)
