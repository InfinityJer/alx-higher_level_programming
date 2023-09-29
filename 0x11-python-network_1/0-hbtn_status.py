#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

# Send a GET request and store the response in a variable
with urllib.request.urlopen(url) as response:
    body = response.read()

# Display information about the response body
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
