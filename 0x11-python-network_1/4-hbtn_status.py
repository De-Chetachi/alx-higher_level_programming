#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
import requests


if __name__ == "__main__":
    '''the script definition'''
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    page = response.text
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
