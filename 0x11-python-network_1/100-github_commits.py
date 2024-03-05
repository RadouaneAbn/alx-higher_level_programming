#!/usr/bin/python3
"""
This script will get the last 10 commits in rails/rails repository
"""
import requests
import sys

user_name, repo = sys.argv[2], sys.argv[1]

# Format the URL
url = f"https://api.github.com/repos/{user_name}/{repo}/commits"

# Send the get request
with requests.get(url) as session:
    if session.status_code != 200:
        print("failed to get the repository")
        sys.exit(1)
    # Store the commit history
    commits = session.json()

# Sort the list of commits in reverse
commits = sorted(commits, key=lambda x: x['commit']['author']['date'],
                 reverse=True)

# Print the last 10 commits
for i in range(10):
    line = commits[i]
    print("{}: {}".format(line['sha'], line['commit']['author']['name']))
