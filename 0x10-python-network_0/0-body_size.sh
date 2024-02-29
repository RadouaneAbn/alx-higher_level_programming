#!/bin/bash
# this script displays the size of the body of a response to a request to a URL
curl -s -w '%{size_download}\n' -o /dev/null "$1"
