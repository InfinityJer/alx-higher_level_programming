#!/bin/bash
# This script sends a POST request to the URL with specific parameters and displays the body of the response

# URL to send the POST request to
url="$1"

# Define the POST data as URL-encoded form parameters
data="email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"

# Send the POST request and display the response body
curl -s -X POST -d "$data" "$url"
