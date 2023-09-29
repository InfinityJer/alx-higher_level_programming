#!/usr/bin/python3
"""
    list 10 commits (from the most recent to oldest) of the repository
    “rails” by the user “rails”
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository name> <owner name>".format(sys.argv[0]))
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL to retrieve commits
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"
    # Send a GET request to the GitHub API
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()

        # Print the 10 most recent commits
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)
