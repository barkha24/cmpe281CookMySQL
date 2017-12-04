#!/usr/bin/bash

# ########################
# Frontend Dependency installer
# for Cloud Project #2
# ########################

if [ ! -f cmpe281p2.tgz ]; then
   echo "Please copy cmpe281p2.tgz file to the current directory"
   exit 1
fi

# Install php and start httpd
echo "Installing services..."
sudo yum install httpd -y
sudo yum install php -y

echo "Starting PHP server..."
service httpd start
sudo chkconfig httpd on

echo "Deploying Application..."
sudo rm -rf /tmp/deploy
sudo tar -xvf cmpe281p2.tgz -C /tmp/deploy

sudo cp -rf /tmp/deploy/frontend/* /var/www/html
echo "Frontend installer complete!"
