#!/bin/bash
# This script sends a JSON POST request to a URL, and displays teh response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
