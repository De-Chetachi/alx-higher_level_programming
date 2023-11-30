#!/bin/bash
# Bash script that takes in a URL, sends a GET request to that URL
curl -si $1 | grep Allow: | sed 's/Allow: //'
