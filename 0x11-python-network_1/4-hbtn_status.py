#!/usr/bin/python3
"""
Python Script fetches https://alx-intranet.hbtn.io/status
"""
import request

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))