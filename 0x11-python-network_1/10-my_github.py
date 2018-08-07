#!/usr/bin/python3
# use github api to retrieve a user's id


if __name__ == '__main__':
    import requests
    from sys import argv
    user = argv[1]
    pw = argv[2]
    url = 'https://api.github.com/user'
    cred = (user, pw)
    r = requests.get(url, auth=cred)
    res = dict(r.json())
    print(res.get('id'))
