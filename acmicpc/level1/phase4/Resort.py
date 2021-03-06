from __future__ import division
import sys
from fractions import Fraction
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
import traceback
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
parents=[]
for i in range(n+1):
    parents.append([])
children=[]
for i in range(n+1):
    children.append([])
objects,tracks=[0],[0] 
objects.extend(read_integers())
tracks.extend(read_integers())
for i in range(1,n+1):
    if tracks[i]!=0:
        parents[i].append(tracks[i])
        children[tracks[i]].append(i)
mxpth=[]
for i in range(1,n+1):
    if objects[i]==1:
        path=[i]
        if len(parents[i])>0:
            current=parents[i][0]
            while len(children[current])==1 :
                path.append(current)
                if len(parents[current])>0:
                    current=parents[current][0]
                else:
                    break
        if len(path)>len(mxpth):
            mxpth=path
print len(mxpth)
print ' '.join([str(x) for x in mxpth][::-1])
            
        
