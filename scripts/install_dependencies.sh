#!/bin/bash
sudo yum update -y
sudo yum install -y nodejs npm
sudo npm install pm2 -g
sudo npm install express
sudo rm -rf /home/ec2-user/my-app1