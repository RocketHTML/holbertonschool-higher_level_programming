#!/bin/bash
# prints the size of the content body of a curl request
domain=$1
curl -sI "$domain" | grep 'Content-Length' | awk '{print $2}'
