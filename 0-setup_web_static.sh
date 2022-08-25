#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
echo 'Hello World!' > /var/www/html/index.nginx-debian.html
service nginx start
touch /data/
touch /data/web_static/
touch /data/web_static/releases/
touch /data/web_static/shared/
touch /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test/
chown ubuntu:ubuntu /data/

#location /data/web_static/current/ {
#	alias hbnb_static;
#	autoindex off;
#}
