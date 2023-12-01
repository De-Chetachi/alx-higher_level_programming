#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests
import sys

if __name__ == "__main__":
    '''the script definition'''
    # url = 'https://alx-intranet.hbtn.io/status'
    url = sys.argv[1]
    # url = url_ + '/post'
    data = {'email': sys.argv[2]}
    response = requests.post(url, data)
    page = response.text
    print('Your email is: {}'.format(page))
