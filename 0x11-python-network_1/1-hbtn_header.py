#!/usr/bin/python3
# This script prints the value of the X-Request-Id variable

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        headers = r.info()
        request_id = headers.get('X-Request-Id', None)
        if request_id:
            print(request_id)
