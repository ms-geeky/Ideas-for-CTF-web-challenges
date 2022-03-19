# git challenge

the idea is to serve the git repo (which is setup by running git.sh) with the same apache server that is also use by "docker-cert-and-git-poc".

In total, there can several flags be found:

1. the first flag can be found on a branch called "secret"
2. the second flag can give a hint to an endpoint in query.sh: http://0.0.0.0:80/asdfadsdfafdg.php (TODO: this php script could yield a flag); it is random enough to not be found by brute dictionary attacks
3. the third flag can be found by running hello.spl as a shakespearelang script! (TODO), right now the spl script only prints "Hello world!", a new line and the character "d"

## Idea for the git challenge: use Shakespearelang

To spice up the git challenge, Shakespearelang could be used: https://de.wikipedia.org/wiki/Shakespeare_Programming_Language

So the participants not only have to find a flag on another branch, but also they have to run the .spl file to find another flag.

For exemplary purposes: 

The lines I added in hello.spl at the bottom print the character "d", because "d" is the ASCII representation of the decimal number "100": 

```Scene III: Macbeth and Ophelia's and conversation.
[Enter Macbeth]
Ophelia:
You are as stupid as the difference between the square of the difference between my little pony and your big hairy hound and the cube of your sorry little codpiece! Speak your mind!
```