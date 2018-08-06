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
    with urllib.request.urlopen(sys.argv[1], data=data) as res:
        content = res.read()
        print(content)
