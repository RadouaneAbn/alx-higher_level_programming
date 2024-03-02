#!/usr/bin/python3
# This script prints the value of the X-Request-Id variable

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        x_request_id = r.headers.get("X-Request-Id", None)
        if x_request_id:
            print(x_request_id)
