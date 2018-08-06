#!/usr/bin/python3
# Handle error response


if __name__ == '__main__':
    import urllib.request as ur
    from urllib.error import URLError, HTTPError
    from sys import argv
    url = argv[1]
    try:
        with ur.urlopen(url) as req:
            html = req.read().decode('utf-8')
            print(html)
    except HTTPError as h:
        print(h.read().decode('utf-8'))
    except URLError as e:
        print('We failed to reach the server')
        print('Reason: ', e.reason)
