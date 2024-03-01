#!/usr/bin/python3
# This script fetches a URL

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
    data = r.read()
output = "Body response:\n\t- type: {}\n\t- content: {}\n\
\t- utf8 content: {}".format(type(data), data, data.decode())
print(output)
