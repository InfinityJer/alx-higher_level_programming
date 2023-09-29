#!/usr/bin/python3
"""
Script Displays value of X-Request-Id variable found in Header response
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

    # Check if the X-Request-Id header is present in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
