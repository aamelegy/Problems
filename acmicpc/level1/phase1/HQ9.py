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
if set(["H","Q","9"]) & set(word):
    writeline("YES")
else:
    writeline("NO")
    