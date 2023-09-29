#!/usr/bin/python3
"""
Displays response body with email passed to URL using POST request
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary to hold the email parameter
    data = {"email": email}

    # Send a POST request to the provided URL with the email parameter
    response = requests.post(url, data=data)

    # Display the body of the response
    print("Your email is:", response.text)
