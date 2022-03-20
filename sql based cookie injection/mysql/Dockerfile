FROM mysql:5.7.37-debian

# TODO: run as non privileged user and get updates

# sql file to setup the database
COPY setupcommands.sql /docker-entrypoint-initdb.d/

# commands to build the image and run as container:

# docker build -t mysqlcustom .
# docker run --rm -it -e MYSQL_ROOT_PASSWORD=shoshohN3Eishah8aegae4phiomoot7u -e MYSQL_DATABASE=flask -p 127.0.0.1:3306:3306 --name mysqlcustom mysqlcustom