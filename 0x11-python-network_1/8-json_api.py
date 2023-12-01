#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":
    '''the script definition'''
    # url = 'https://alx-intranet.hbtn.io/status'
    url = 'http://0.0.0.0:5000/search_user'
    try:
        a = sys.argv[1][0]
    except IndexError:
        a = ''
    # url = url_ + '/post'
    da = {'q': a}
    r = requests.post(url, data=da)
    try:
        arr = r.json()
        if arr:
            print('[{}] {}'.format(arr.get('id'), arr.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
