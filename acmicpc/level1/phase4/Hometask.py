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

n=read_integer()
num=read_integers()
num.sort()
sm=sum(num)
md=sm%3
md1=[i for i,x in enumerate(num) if x%3==1]
md2=[i for i,x in enumerate(num) if x%3==2]
if num[0]!=0:
    writeline(-1) ; end()
if sm==0:
    writeline(0) ;end()
if md==0 :
    writeline(''.join([str(x) for x in num])[::-1])
else:
    if md==1 and len(md1)>0:
        del num[md1[0]]
    elif md==1 and len(md2)>1:
        del num[md2[0]]
        del num[md2[1]-1]
    elif md==2 and len(md2)>0:
        del num[md2[0]]
    elif md==2 and len(md1)>1:
        del num[md1[0]]
        del num[md1[1]-1]
    else:
        writeline(-1); end()
    if sum(num)==0:
        writeline(0); end()
    writeline(''.join([str(x) for x in num])[::-1])
        
        
        
        
    

    

        
        
        
    