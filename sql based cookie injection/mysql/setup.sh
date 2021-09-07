#!/bin/bash

# docker exec --rm -it mysqlcustom bash

# login as root with
# mysql -p
# shoshohN3Eishah8aegae4phiomoot7u

CREATE database flask;
USE flask;
CREATE TABLE queue(userID VARCHAR(32) NOT NULL,queueNum INT(11),PRIMARY KEY(userID));
CREATE TABLE flag(flag VARCHAR(32) NOT NULL);
INSERT INTO flag VALUE("BIT{yayy_y0u_g0t_appl3_ic3}");
create user 'flask'@'%'identified by 'v5UmnxifRv';
# reload privileges
FLUSH PRIVILEGES;
GRANT SELECT ON flask.* TO 'flask'@'%'; 