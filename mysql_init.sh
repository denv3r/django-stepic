sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE django;"
mysql -uroot -e "SHOW DATABASES;"