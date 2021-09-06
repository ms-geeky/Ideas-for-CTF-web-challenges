#!/bin/bash



# generate ca key and cert
openssl req -config ca_openssl.conf -x509 -new -nodes -newkey rsa -keyout ca.key -days 3650 -out ca.crt 

# create databases files for ca
touch serial.txt
touch index.txt
touch rand

# create server key
openssl genrsa -out server.key 2048 
openssl req -new -key server.key -subj /CN=localhost -out server.csr
# let server cert be signed by CA
openssl ca -batch -config ca_openssl.conf -keyfile ca.key -cert ca.crt -policy signing_policy -out server.crt -infiles server.csr 

# create client cert and p12 store; only O=BIT is important!
openssl genrsa -out client.key 2048 
openssl req -new -key client.key -subj /CN=Haxxorman/C=US/O=BIT -out client.csr
# let client cert be signed by CA
openssl ca -batch -config ca_openssl.conf -keyfile ca.key -cert ca.crt -policy signing_policy -out client.crt -infiles client.csr 
# export client key and cert to p12 store
openssl pkcs12 -export -inkey client.key -in client.crt -out client.p12 -passin pass:test123 -passout pass:test123