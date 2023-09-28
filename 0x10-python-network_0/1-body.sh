#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body if the status code is 200
curl -sL "$1"
