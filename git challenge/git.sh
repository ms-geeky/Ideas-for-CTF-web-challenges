#!/bin/bash

#script for the .git challenge

git config --global user.name "ms.geeky";

git config --global user.email "ms.geeky@localhost"; 

git init;

echo "sth" > hello.txt;

git add hello.txt;

git commit -m "organized with object (app)";

rm hello.txt;

git commit -m "fix";

echo "Did you think it was gonna be this easy?" > README.md;

git add README.md

git commit -m "Update README.md"

git branch -m secret;

git commit -m "created new branch secret";

git tag v1.0.0;

git branch secret;

git checkout secret;

echo "BIT{exp0s3d_g1t_r3po}" > flag.txt;

git add flag.txt;

git commit -m "added flag.txt"

rm flag.txt;

git commit -m "removed flag.txt";

git branch master;

git checkout master;

echo "<?php echo "Hello World!"; ?>" > test.php;

git add test.php;

git commit -m "added test.php";

git branch main;

git checkout main;

git add query.sh;

git commit -m "added script to query local webserver";

git add shakespearelang/hello.spl;

git commit -m "added spl script";
