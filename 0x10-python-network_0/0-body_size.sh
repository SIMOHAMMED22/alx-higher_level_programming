#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1

response=$(curl -s -o /dev/null -w "%{size_download}" "http://$url")

if [ $? -ne 0 ]; then
  echo "Error: Failed to fetch the URL."
  exit 1
fi

echo "Size of the body of the response from $url is: $response bytes"
