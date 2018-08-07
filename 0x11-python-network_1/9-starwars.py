#!/usr/bin/python3
# query starwars api with requests


if __name__ == '__main__':
    import requests
    from sys import argv
    url = 'https://swapi.co/api/people/'
    string = '{}'.format(argv[1])
    post = {'search': string}
    r = requests.get(url, params=post)
    result = dict(r.json())
    rlist = result['results']
    print('Number of results: {}'.format(result['count']))
    for d in rlist:
        print('{}'.format(d['name']))
