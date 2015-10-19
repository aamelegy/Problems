from __future__ import division
import sys
from fractions import Fraction
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
from collections import Counter #Counter(list)
import re #re.split("[^a-zA-Z]",text)
# from functools import lru_cache #@lru_cache(maxsize = None)

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
def end():
    sys.exit()
num=[x for x in readline()]
c=Counter(num)
if c['4'] ==0 and c['7']==0:
    writeline(-1) ; end()
if c['4'] >= c['7']:
    writeline(4)
else:
    writeline(7)