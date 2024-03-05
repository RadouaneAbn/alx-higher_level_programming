#!/usr/bin/python3
"""
This script will get the last 10 commits in rails/rails repository
"""
import requests
import sys


if __name__ == "__main__":
    # Format the URL
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    # Send the get request and store the commit history
    with requests.get(url) as session:
        commits = session.json()

    try:
        for i in range(10):
            line = commits[i]
            print("{}: {}".format(line['sha'],
                                  line['commit']['author']['name']))
    except IndexError:
        pass
