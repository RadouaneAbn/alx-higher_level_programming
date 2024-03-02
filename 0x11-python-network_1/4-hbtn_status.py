#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    output = "Body response:\n\t- type: {}\n\t- content: {}".format(
            type(res.text), res.text)
    print(output)
