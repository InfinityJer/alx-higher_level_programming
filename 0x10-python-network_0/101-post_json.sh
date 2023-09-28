#!/bin/bash
# Send the JSON POST request and display the response body
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
