
from __future__ import division
import sys
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
"""
#reduce(func,list)
#map(func,list)
#filter(func,list)
#xor=lambda x,y :x^y
#sign = lambda x: math.copysign(1, x)
#list.reverse() 
#list.sort() sorted(list)
#reverse word word[::-1]
#word.islower()
#word.lower() word.upper()
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


word=readline()
if "0000000" in word or "1111111" in word:
    writeline("YES")
else:
    writeline("NO")