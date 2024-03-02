#!/usr/bin/python3
"""
This script takes a url and an email, sends a POST request to the url
with the parameter, and display the body of the response
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    info = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(info).encode()
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as r:
        response = r.read().decode('utf8')

    print(response)
