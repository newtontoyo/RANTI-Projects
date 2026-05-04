FROM alpine:3.19

RUN apk update && apk add --no-cache \
    nginx \
    php81 \
    php81-fpm \
    php81-mysqli \
    php81-pdo \
    php81-pdo_mysql \
    php81-json \
    php81-mbstring \
    php81-session

# PHP-FPM foreground mode
RUN sed -i 's/;daemonize = yes/daemonize = no/' /etc/php81/php-fpm.conf

# Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Web root
RUN mkdir -p /var/www/html
COPY app /var/www/html

EXPOSE 80

CMD php-fpm81 -D && nginx -g "daemon off;"

