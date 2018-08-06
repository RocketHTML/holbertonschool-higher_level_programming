#!/usr/bin/python3
'''fetch cmdline url, and display X-Request-Id header'''


if __name__ == '__main__':
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.info()['X-Request-Id']
        print(header)
