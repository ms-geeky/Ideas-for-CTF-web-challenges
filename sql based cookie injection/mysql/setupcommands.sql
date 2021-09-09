-- create "flag" table
CREATE TABLE (NT3PDPbcTm2k969w VARCHAR(32) NOT NULL);
INSERT INTO NT3PDPbcTm2k969w VALUE("BIT{yayy_y0u_g0t_appl3_ic3}");

-- create all other tables
CREATE TABLE ice_flavors (flavors VARCHAR(32),quantity INT, price INT);
CREATE TABLE products (products VARCHAR(32),discount_percent INT, price INT);
CREATE TABLE cakes_and_desserts (products VARCHAR(32),quantity INT, price INT);
CREATE TABLE soda (soda_flavor VARCHAR(32),quantity INT, price INT);

INSERT INTO ice_flavors VALUE("chocolate",90,60);
INSERT INTO ice_flavors VALUE("butterscotch",100,55);
INSERT INTO ice_flavors VALUE("strawberry",110,40);

create user 'flask'@'%'identified by 'v5UmnxifRv';
# reload privileges
FLUSH PRIVILEGES;
GRANT SELECT ON flask.* TO 'flask'@'%'; 