#!/usr/bin/python3
"""
Displays body of response but also manages HTTPErrors
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Send a GET request to the provided URL using the requests package
    response = requests.get(url)

    # Display the body of the response
    print(response.text)

    # Check the HTTP status code and print an error message if >= 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
