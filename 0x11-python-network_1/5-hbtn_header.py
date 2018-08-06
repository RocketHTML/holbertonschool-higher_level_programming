#!/usr/bin/python3
# Extract the header X-Request-Id using requests


if __name__ == '__main__':
    import requests
    import sys
    r = requests.get(sys.argv[1])
    xreqheader = r.headers.get('X-Request-Id')
    print(xreqheader)
