sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo pkill gunicorn
sudo gunicorn hello:wsgi_application --bind 0.0.0.0:8000 &
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000 &