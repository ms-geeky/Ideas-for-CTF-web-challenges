# CTF web challenges

this repo consists of several challenge ideas for a CTF, all based around web challenges.

All can be run in docker containers, where the git and cert challenge run in the same container (docker-cert-and-git-poc).

The first challenge consists of a "sql based cookie injection", using flask as a webserver and mysql as the database. [challenge 1](sql%20based%20cookie%20injection/README.MD)

The second challenge resolves around git. [challenge 2](git%20challenge/README.MD)

The third challenge is about authenticating with a client cert with a certain "Subject" field in the cert which the ctf players have to sign with the openly available "CA" private key! [challenge 3](docker-cert-and-git-poc/README.MD)

Copyright © 2022 Swetha Sridevi Nachimuthu
