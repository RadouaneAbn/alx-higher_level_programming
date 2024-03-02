#!/usr/bin/python3
"""
This script that takes your GitHub credentials (username and password) and
uses the GitHub API to display my id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=basic)
    res_json = res.json()
    print(res_json.get("id"))
