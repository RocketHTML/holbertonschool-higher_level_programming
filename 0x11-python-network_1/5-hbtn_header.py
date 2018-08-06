#!/usr/bin/python3
# Extract the header X-Request-Id using requests


if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    xreqheader = r.headers['X-Request-Id']
    print(xreqheader)
