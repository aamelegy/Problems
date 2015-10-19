import sys
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

n=read_integer()
l=read_integers()
cl=Counter(l)
groups=[[1,3,6],[1,2,4],[1,2,6]]
count=[0,0,0]
for i,group in enumerate(groups):
    count[i]=min(cl[group[0]],cl[group[1]],cl[group[2]])
    for j in group:
        cl[j]-=count[i]
if sum(count)*3<n:
    writeline("-1")
    end()
for i,group in enumerate(groups):
    for j in range(count[i]):
        writeline(' '.join([str(x) for x in group]))
    

