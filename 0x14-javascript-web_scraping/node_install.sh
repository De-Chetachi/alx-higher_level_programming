#!/usr/bin/bash
#install node

curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install semistandard --global
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
