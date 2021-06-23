sudo mv uptime-py /usr/bin/uptim-py
sudo mv web /var/www/html

crontab -l | { cat; echo "*/1 * * * * /usr/bin/python3 /usr/bin/uptime-py/ping.py"; } | crontab -
