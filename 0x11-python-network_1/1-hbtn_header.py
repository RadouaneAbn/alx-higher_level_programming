#!/usr/bin/python3
# This script prints the value of the X-Request-Id variable

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as r:
    request_id = r.headers.get('X-Request-Id')
    print(request_id)
