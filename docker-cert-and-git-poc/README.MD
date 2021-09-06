## poc for apache running in docker with accessible .git on port 80 (http) and client cert "protected" flag on port 443 (https)

### how to run it

first, generate CA files with openssl, generate a server cert for apache and a client cert for your browser with the script generatekeysandcerts.sh. Now, put your git project folder (.git) into the folder git, so it gets copied.

Then you can build the docker image and run it:

```docker build -t phptest .```

```docker run --rm -it -p 127.0.0.1:443:443 -p 127.0.0.1:80:80 --name phptest phptest```

On port 80, there is only .git accessible.

On port 443, the flag at /protected/index.php is only accessible when you use a client cert with the Subject (import the p12 file into your browser as your client cert; it will ask for your client cert when you visit /protected). Otherwise, there is a 403 redirect to clientcertneeded.php which gives you info on what to do.