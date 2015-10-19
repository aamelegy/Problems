import sys
from collections import deque
def readline():
    return sys.stdin.readline().strip()
def writeline(value):
    sys.stdout.write(str(value))
    sys.stdout.write("\n")
def read_integers():
    return [int(x) for x in sys.stdin.readline().strip().split(' ')]
def read_integer():
    return int(sys.stdin.readline().strip())


word=readline()
up=0
for ch in word:
    if not ch.islower():
        up+=1
if up==len(word)-1 and word[0].islower():
    word=word[0].upper()+word[1:].lower()
if up==len(word):
    word=word.lower()
writeline(word)