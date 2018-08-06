#!/usr/bin/python3
# Takes in a URL and an email, then posts email to URL
# Displays the body of the request afterwards


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as res:
        content = res.read().decode('utf-8')
        print(content)
