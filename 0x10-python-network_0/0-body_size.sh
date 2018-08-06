#!/bin/bash
# prints the size of the content body of a curl request
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
