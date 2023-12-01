#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":
    '''the script definition'''
    # url = 'https://alx-intranet.hbtn.io/status'
    url = sys.argv[1]
    response = requests.get(url)
    it = response.headers['X-Request-Id']
    print(it)
