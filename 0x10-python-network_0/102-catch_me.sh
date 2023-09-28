#!/bin/bash
# Send the request and include a custom header to trigger the response
curl -s -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" "0.0.0.0:5000/catch_me"
