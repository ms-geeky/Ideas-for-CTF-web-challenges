#!/bin/bash

#script for the .git challenge

git config --global user.name "ms.geeky";

git config --global user.email "ms.geeky@localhost"; 

git clone https://github.com/jofpin/hubpi.git;

cd hubpi;

rm -rf .git;

git init;

git add index.html;

git commit -m "Update index.html";

git add .;

git commit -m "added files";

echo "nothing" > pineres.min.css;

git add pineres.min.css;

git commit -m "added pineres.min.css";

rm pineres.min.css;

git commit "deleted pineres.min.css";

echo "nothing" > i.min.css;

git add i.min.css;

git commit -m "added i.min.css";

rm i.min.css;

git commit -m "deleted i.min.css";

echo "nothing" > styles.css;

git add styles.css;

git commit -m "update styles.css";

rm styles.css;

git commit -m "deleted styles.css"

echo "text-overflow: ellipsis;" > post.css;

git add post.css;

git commit -m "postCSS v1.0.0 :smile:"

rm post.css;

git commit -m "update post.css";

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
