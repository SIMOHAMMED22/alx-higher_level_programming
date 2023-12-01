#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.
url=$1
status_code=$(curl -s -o /dev/null -w "%{http_code}" $url)
echo "Status code: $status_code"
