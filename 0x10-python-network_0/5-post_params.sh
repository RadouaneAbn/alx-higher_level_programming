#!/bin/bash
# This script sends a POST request to the passed URL, and displays teh body of the response
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
