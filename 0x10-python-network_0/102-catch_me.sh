#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me and displays the response
curl -X PUT -L -H "Origin: HolbertonSchool" -s 0.0.0.0:5000/catch_me -d 'user_id=98'
