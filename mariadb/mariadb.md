# Update your arch linux.
- sudo pacman -Syu
# Install the mariadb system.
- sudo pacman -S mariadb
# Installing the mariadb database in our system.
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
# If you want a safe installation of the mariadb system.
sudo mysql_secure_installation  # For secure installation for the database managment system.
# Stating the mariadb system services.
sudo systemctl start mariadb
sudo systemctl enable mariadb

# Using the mariadb root user accout to login.
sudo mariadb -u root -p

# Creating a database using the root user accout.
CREATE DATABASE my_database;
CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'my_password';
GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Using my own user accout to login.
mariadb -u my_user -p my_database

# Configration file for the mariadb.
sudo vi /etc/mysql/my.cnf
bind-address = 0.0.0.0

# Restarting mariadb services.
sudo systemctl restart mariadb

# Using to root accout.
sudo mariadb -u root -p

# Granting the user privileges on a database.
GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'%' IDENTIFIED BY 'my_password';
FLUSH PRIVILEGES;
EXIT;

# Giving the firewall.
sudo ufw allow 3306/tcp
