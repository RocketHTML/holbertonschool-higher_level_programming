#!/usr/bin/python3
# handle json using requests


if __name__ == '__main__':
    import requests
    from sys import argv
    q = argv[1] if len(argv) > 1 else ""
    post = {'q': q}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=post)
    try:
        j = r.json()
        if len(j) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except ValueError as v:
        print('Not a valid JSON')
