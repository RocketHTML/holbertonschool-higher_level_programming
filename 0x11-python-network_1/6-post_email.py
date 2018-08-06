#!/usr/bin/python3
# send a post request containing an email, using requests


if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    data = {'email': argv[2]}
    r = requests.get(url, data=data)
    print(r.text)
