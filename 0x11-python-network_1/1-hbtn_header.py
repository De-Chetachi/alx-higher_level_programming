#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import urllib.request
import sys

if __name__ == "__main__":
    '''the script definition'''
    #url = 'https://alx-intranet.hbtn.io/status'
    url = sys.argv[1]
    quest = urllib.request.Request(url)
    with urllib.request.urlopen(quest) as response:
        info_dict = response.info()
        print(info_dict['X-Request-Id'])
