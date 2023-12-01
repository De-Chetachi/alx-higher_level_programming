#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    '''the script definition'''
    # url = 'https://alx-intranet.hbtn.io/status'
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    quest = urllib.request.Request(url, data)
    with urllib.request.urlopen(quest) as response:
        page = response.read()
        email = page.decode('utf-8')
        print('Your email is: {}'.format(email))
