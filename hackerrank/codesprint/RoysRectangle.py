import sys
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
from collections import Counter #Counter(list)
import re #re.split("[^a-zA-Z]",text)
# from functools import lru_cache #@lru_cache(maxsize = None)
"""
#reduce(func,list)
#map(func,list)
#filter(func,list)
#xor=lambda x,y :x^y
#sign = lambda x: math.copysign(1, x)
#list.reverse() 
#list.sort() list=sorted(list)
list.sort(key=operator.itemgetter(1,2))
#reverse word word[::-1]
#word.islower()
#word.lower() word.upper()
x = x1 if exp1 else x2
any([false,true])
all([true,false])
"a".isalpha()
"1".isdigit()
int(str,base)
"""

fin=sys.stdin ;fout=sys.stdout 
# fin=open('../in','r') ; fout=open('../out','w')
def readline():
    return fin.readline().strip()
def readstrings():
    return fin.readline().strip().split(' ')
def writeline(value):
    fout.write(str(value))
    fout.write("\n")
def read_integers():
    return [int(x) for x in fin.readline().strip().split(' ')]
def read_integer():
    return int(fin.readline().strip())

t=read_integer()
for _ in range(t):
    x,y,x1,y1,x2,y2=read_integers()
    print min(abs(x1-x),abs(x2-x),abs(y1-y),abs(y2-y))

