#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable found in Header response
"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Send a GET request to the provided URL and store the response
    with urllib.request.urlopen(url) as response:
        headers = response.info()

    # Find and display the value of the X-Request-Id header
    x_request_id = headers.get("X-Request-Id")
    if x_request_id:
        print(x_request_id)
