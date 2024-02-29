#!/bin/bash
# This script displays the status code of a response to a request to a URL
curl -s -w '%{http_code}' -o /dev/null "$1"
