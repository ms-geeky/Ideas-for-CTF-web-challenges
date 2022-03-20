FROM php:8.0-apache

# get updates
RUN apt update && \
    apt upgrade -y

WORKDIR /var/www/html

COPY index.php index.php

RUN mkdir .git && mkdir protected

COPY .git .git/

ADD protected ./protected

COPY server.key /etc/ssl/private/
COPY server.crt /etc/ssl/certs/
COPY ca.crt /etc/ssl/certs/
COPY ca.key /etc/ssl/certs/ca

COPY clientcertneeded.php ./

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf 

# remove default confs
#RUN rm /etc/apache2/sites-available/000-default.conf && rm rm /etc/apache2/sites-available/default-ssl.conf

COPY localhost.conf /etc/apache2/sites-available/

RUN chmod -R a+r /etc/ssl/certs

# still todo: add user and group with lowest privileges possible and run the container with that!

CMD ["sh","-c","apache2-foreground & sleep 5 && a2dissite 000-default && a2ensite localhost && a2enmod ssl && a2enmod rewrite && a2enmod autoindex && service apache2 reload && (while true; do sleep 10; done)"]
