FROM mysql:8.0.26


COPY setupcommands.sql /docker-entrypoint-initdb.d/

# docker build -t mysqlcustom .
# docker run --rm -it -e MYSQL_ROOT_PASSWORD=shoshohN3Eishah8aegae4phiomoot7u -e MYSQL_DATABASE=flask -p 127.0.0.1:3306:3306 --name mysqlcustom mysqlcustom