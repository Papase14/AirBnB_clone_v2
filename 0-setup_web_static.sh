#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# Update and upgrade packages
sudo apt-get -y update
sudo apt-get -y upgrade

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test HTML file
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

# Create or update the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to the ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data/

# Add a location block for /hbnb_static to Nginx config
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Start Nginx
sudo service nginx start

exit 0