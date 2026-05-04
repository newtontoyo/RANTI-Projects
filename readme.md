Overview
This project provides a lightweight, production‑sane setup for running:

PHP‑FPM (PHP 8.1)

Nginx

MySQL 8.0

The PHP‑FPM and Nginx services run inside the same container, while MySQL runs in a separate container. The PHP application can insert, read, and delete entries from the MySQL database.

The stack is orchestrated using Docker Compose.

PROJECT STRUCTURE

project/
│
├── Dockerfile
├── nginx.conf
├── docker-compose.yml
└── app/
    └── index.php
COMPONENTS

1. PHP‑FPM + Nginx Container

   Alpine‑based image

   PHP‑FPM runs in foreground mode

   Nginx proxies .php files to PHP‑FPM

   Includes MySQL extensions (mysqli, pdo_mysql)

2. MySQL Container
   MySQL 8.0

   Exposes port 3306

   Auto‑creates database + use

INSTALLATION AND SETUP
1. Clone REPO
git clone <your-repo-url>
cd project

2. Build and Start Containers

docker-compose up --build

3. Access the Application

http://localhost:8080
4. Setup Database

After the MYSQl container starts, create required table

docker exec -it mysql_db mysql -u root -p

Then Run

CREATE TABLE myapp.people (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);



Testing the App
The UI supports:

Adding a name

Listing all names

Deleting a name

All operations are performed through MySQL from the PHP‑FPM + Nginx container.

Configuration Details
docker-compose.yml
Defines two services:

web → PHP‑FPM + Nginx

db → MySQL

The web container connects to MySQL using hostname: db

Dockerfile
Builds the combined PHP‑FPM + Nginx container.

nginx.conf
Routes PHP requests to PHP‑FPM on port 9000.

Useful Docker Commands

docker ps
docker-compose down
docker-compose build --no-cache

Troubleshooting

MySQL connection errors
Ensure MySQL is fully started:

docker logs mysql_db

403 or 404 errors
Ensure app/index.php exists.

Ensure Nginx root path matches /var/www/html.

PHP not executing
Confirm PHP‑FPM is running:

docker exec -it php_nginx ps aux



Notes
This setup is ideal for local development or lightweight deployments.

For production, consider:

Separate containers for PHP‑FPM and Nginx

Non‑root users

Persistent MySQL volumes

HTTPS termination
