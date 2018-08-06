#!/usr/bin/python3
# Handle http error with requests


if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print('Error code: ', end='')
        print(e.response.status_code)
