#!/bin/bash
# This script displays all HTTP methods the server will accept
curl -s --head "$1" | grep "Allow" | cut -c 8-
