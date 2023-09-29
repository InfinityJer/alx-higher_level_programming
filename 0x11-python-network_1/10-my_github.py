#!/usr/bin/python3
"""
Takes GitHub credentials and uses the Github API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    # Create a Basic Authentication header using the personal access token
    auth = (username, token)

    # Define the GitHub API URL to access your user information
    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        # If the response status code is 200, display the user ID
        user_data = response.json()
        print(user_data.get("id"))
    else:
        # If the response status code is not 200, print None
        print("None")
