#!/bin/bash


# openssl req -newkey rsa:2048 -x509 -nodes -keyout server.key -new -out server.crt -subj /CN=localhost -sha256 -days 3650

# generate ca key and cert
openssl req -newkey rsa:2048 -nodes -keyform PEM -keyout ca.key -x509 -days 3650 -outform PEM -subj /CN=CA -out ca.crt 

# create server key
openssl genrsa -out server.key 2048 
openssl req -new -key server.key -subj /O=BIT -out server.csr
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -set_serial 100 -days 365 -outform PEM -out server.crt 

# create client cert and p12 store; only O=BIT is important!
openssl genrsa -out client.key 2048 
openssl req -new -key client.key -subj /CN=Haxxorman/C=US/O=BIT -out client.csr
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -set_serial 100 -days 365 -outform PEM -out client.crt 
openssl pkcs12 -export -inkey client.key -in client.crt -out client.p12 -passin pass:test123 -passout pass:test123