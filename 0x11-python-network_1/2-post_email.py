#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary to hold the email parameter
    data = {"email": email}
    data = urllib.parse.urlencode(data).encode("utf-8")

    # Send a POST request to the provided URL with the email parameter
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode("utf-8")

    # Display the body of the response
    print(body)
