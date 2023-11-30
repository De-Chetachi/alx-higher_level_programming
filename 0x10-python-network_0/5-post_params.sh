#!/bin/bash
# Bash script that takes in a URL, sends a GET request to that URL
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" $1
