## poc for apache running in docker with accessible .git on port 80 (http) and client cert "protected" flag on port 443 (https)

### how to run it

first, generate CA files with openssl, generate a server cert for apache and a client cert for your browser with the script generatekeysandcerts.sh. Now, create a folder "git" and put your git project folder (.git) into the folder git, so it gets copied by the docker build command.

Then you can build the docker image and run it:

```docker build -t phptest .```

```docker run --rm -p 127.0.0.1:443:443 -p 127.0.0.1:80:80 --name phptest phptest```

On port 80, there is only .git accessible.

Command to recursively get the .git files and display the logs:

```mkdir -p ~/Downloads/git/.git && cd ~/Downloads/git/.git && wget -r -nH --cut-dirs=1 --no-parent --reject="index.html*" http://127.0.0.1:80/.git && cd ~/Downloads/git && git log```

On port 443, the flag at /protected/index.php is only accessible when you use a client cert with the Subject (import the ca.crt as a trusted authority and the p12 file into your browser as your client cert; it will ask for your client cert when you visit /protected). Otherwise, there is a 403 redirect to clientcertneeded.php which gives you info on what to do.

Example with curl:

We have to use "insecure", otherwise we would need to add our ca.crt to the systems certificate truststore (where all the ca files reside) first.

```curl --insecure -E ./client.crt --key ./client.key https://127.0.0.1:443/protected/``` 

To get some info about your cert you can go to (certdata.php can be adjusted as pleased):

```curl --insecure -E ./client.crt --key ./client.key https://127.0.0.1:443/protected/certdata.php``` 
