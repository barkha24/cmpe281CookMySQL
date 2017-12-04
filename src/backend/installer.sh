#!/usr/bin/env bash

# ########################
# Backend Dependency installer
# for Cloud Project #2
# ########################

if [ "$1" == "" ]; then
   echo "Please providethe following arguments:"
   echo "aws-key aws-id aws-secret mysqlpasswrd"
   exit 1
fi

if [ ! -f cmpe281p2.zip ]; then
   echo "Please copy cmpe281p2.zip file to the current directory"
   exit 1
fi

echo "Install package dependencies"
sudo yum install mariadb -y
sudo yum install python-devel -y
sudo yum install mysql-devel -y
sudo yum install gcc -y

echo "Installing python packages"
sudo pip install boto3
sudo pip install dnspython
sudo pip install MySQL-python

echo "Deploying Application..."
sudo rm -rf /tmp/deploy
sudo mkdir /tmp/deploy
sudo unzip cmpe281p2.zip -d /tmp/deploy

sudo rm -rf /cmpe281p1
sudo mkdir -p /cmpe281p2
sudo cp -rf /tmp/deploy/backend/ /cmpe281p2
sudo cp -rf /tmp/deploy/server /cmpe281p2
sudo cp -rf /tmp/deploy/flaskapp.py /cmpe281p2

echo "Backend installer complete!"
sudo pip install flask
pip install flask_cors
sudo pip install flask_cors
sudo pip install flask_api

export PYTHONPATH=/cmpe281p2:$PYTHONPATH
AWS_ACCESS_ID=$1 AWS_SECRET_KEY=$2 MYSQL_PASS=$3 /cmpe281p2/flaskapp.py
