#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.


# 1. install nginx
sudo apt-get update
sudo apt-get -y install nginx

#.2 create required directoris
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html


#. create a fake html page
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html


#. 4 create symbolic likn
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#. 5 ceate user
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a \tlocation /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# text nginx

sudo ngix -t
sudo service nginx restart
