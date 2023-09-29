#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a request to the provided URL and store the response
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTPError exceptions and print the error code
        print("Error code:", e.code)
