#shakespeare run my-program.spl
#shakespeare debug my-program.spl
#shakespeare console # or just "shakespeare" unadorned
import shakespearelang.repl
from shakespearelang import *

text = ""

with open("hello.spl") as file:
    text = file.read()

#parser = shakespeare_interpreter.shakespeareParser

#parser.parse(text)

shakespeare = shakespearelang.repl.debug_play(text=text)

print("")