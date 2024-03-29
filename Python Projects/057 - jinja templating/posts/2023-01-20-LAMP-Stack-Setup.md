---
title: LAMP Stack Setup
date: 2023-01-23 01:40:00 -0500
categories: [Resources, Bash, Walkthrough]
tags: [linux, servers, apache, nginx, mysql, php-fpm]
published: true
---

LAMP is a bundle of 4 different software technologies that developers use to build websites and application. LAMP is an acronym for the operating system, Linux; the web server, Apache; the database server, MySQL; and the programming language, PHP.

So going to practice some server setup for linux administration for practice.

We are going to setup a network of 4 computers and a load balancer which will help us manage traffic and suggest which server the user should communicate with. 

- 1 Load Balancer with HAProxy
- 2 or more Web Servers with Nginx + PHP-FPM + Laravel and Jetstream installed
- 2 database servers with #MySQL replication
- 1 Redis server to store your #PHP sessions
- NFS server to store your files on

![Stack Setup](/assets/stack-setup.png)


## Table of Contents:

1. [How to How to Setup nginx, PHP, and PHP-FPM](#how-to-setup-nginx-php-and-php-fpm)
2. 


## How to Setup nginx, PHP, and PHP-FPM

1. [Install Nginx on Ubuntu](#install-nginx-on-ubuntu).
2. [Install the php-fpm for Nginx package](#install-the-php-fpm-packages).
3. [Edit the server’s default config file to support PHP in Nginx](#add-php-support-to-nginx).
4. [Add a new pool configuration file](#add-a-new-pool-configuration-file).
5. [Add a PHP file to Nginx’s html directory, Test the PHP, Nginx and PHP-FPM configuration.](#add-a-php-file-to-nginxs-html-directory).

Before continueing we need to make sure packages are good to go.

```bash
apt update
apt upgrade
```

### Install nginx on ubuntu


nginx like Apache is a webserver that is used to host files that are accessible to the internet. I am using [lubuntu](https://lubuntu.me/) installed on a couple different vms for this.

```bash
apt install nginx
```

and verify the server is operational

```bash
systemctl status nginx
```

### Install the php-fpm packages 

We can install php-fpm with the apt-get command. We have to make sure we install php-fpm and not php for conflicts will arise, it will install apache2 which will conflict with our nginx installation.

```bash
apt install php8.1-fpm php8.1-common php8.1-mysql php8.1-xml php8.1-xmlrpc php8.1-curl php8.1-gd php8.1-imagick php8.1-cli php8.1-dev php8.1-imap php8.1-mbstring php8.1-opcache php8.1-redis php8.1-soap php8.1-zip -y
```

and make sure the service is running

```bash
systemctl status php8.1-fpm
```

### Add PHP Support to nginx

We will edit the default nginx config file located at `/etc/nginx/sites-available/default`. This will allow the PHP FastCGI Process Managaer to handle requests that have a .php extension.

We will make the following changes to the Nginx config to support PHP and PHP-FPM on the server:

- Add index.php to the index list.
- Uncomment the PHP scripts to FastCGI entry block.
- Uncomment the line to include snippets/fastcgi-php.conf.
- Uncomment the line to enable the fastcgi_pass and the php8.1-fpm. sock.
- Uncomment the section to deny all access to Apache .htaccess files

```bash
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # SSL configuration
        #
        # listen 443 ssl default_server;
        # listen [::]:443 ssl default_server;
        #
        # Note: You should disable gzip for SSL traffic.
        # See: https://bugs.debian.org/773332
        #
        # Read up on ssl_ciphers to ensure a secure configuration.
        # See: https://bugs.debian.org/765782
        #
        # Self signed certs generated by the ssl-cert package
        # Don't use them in a production server!
        #
        # include snippets/snakeoil.conf;

        root /var/www/wordpress/html;

        # Add index.php to the list if you are using PHP
        index index.php index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }

        # pass PHP scripts to FastCGI server
        #
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
        #
        #       # With php-fpm (or other unix sockets):
                fastcgi_pass unix:/run/php/php8.1-fpm-wordpress.sock;
        #       # With php-cgi (or other tcp sockets):
        #       fastcgi_pass 127.0.0.1:9000;
        }

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        location ~ /\.ht {
        #       deny all;
        #}
}
```
{: file="/etc/nginx/sites-available/default" }

We can validate a nginx config file with `nginx -t`

```bash
root@0xskar-webserver01:/home/oskar# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

### Add a PHP file to Nginx’s html directory

We can add info.php to the webdirectory to check everything is working correctly

```php
<?php echo phpinfo();?>x
```
{: file="/var/www/wordpress/html/info.php" }

### Add a new pool configuration file

Visit `/etc/php/8.1/fpm/pool.d` and copy `www.conf` into a new file for example wordpress.conf and edit it to your prefrences. Just make sure to change the pool name and the listen to use the correct sock.

We can also add some custom enviromental variables here to make sure we everything is working correctly.

```bash
...
...
...
env[HOSTNAME] = $HOSTNAME
env[TMP] = /tmp
```
{: file="/etc/php/8.1/fpm/pool.d/wordpress.conf" }

Upon doing all of this we can restart all of the services and visit the `info.php`. Should see at the top the server API is using FPM/FastCGI.

![lamp php-fpm setup](/assets/lamp-stack-php-fpm02.png)

We can do this again lets say for a joomla user and install a joomla website for them.

I've done this on one server with a wordpress at home.osk and a joomla site at joomla.home.osk, also another wordpress site at home2.osk on another nginx server. Going to setup mysql replication now.
