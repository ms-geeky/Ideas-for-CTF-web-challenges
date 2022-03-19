# CTF web challenges

this repo consists of several challenge ideas for a CTF, all based around web challenges.

All can be run in docker containers, where the git and cert challenge run in the same container (docker-cert-and-git-poc).

The first challenge consists of a "sql based cookie injection", using flask as a webserver and mysql as the database. [1](sql based cookie injection/README.md)

The second challenge resolves around git. [2](git challenge/README.md)

The third challenge is about authenticating with a client cert with a certain "Subject" field in the cert which the ctf players have to sign with the openly available "CA" private key! [3](docker-cert-and-git-poc/README.md)