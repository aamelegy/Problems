
from __future__ import division
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
#list.sort() sorted(list)
#reverse word word[::-1]
#word.islower()
#word.lower() word.upper()
x = x1 if exp1 else x2
any([false,true])
all([true,false])
"a".isalpha()
"1".isdigit()
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
def write(value):
    fout.write(str(value))
def line():
    fout.write("\n")


n,m=read_integers()
draw=[]
x1=51 ;y1=51;x2=0;y2=0
for i in range(n):
    draw.append([x for x in readline()])
for i in range(n):
    for j in range(m):
        if draw[i][j]=="*":
            x1=min(x1,i) ; y1 =min(y1,j) ;x2=max(x2,i);y2=max(y2,j)
for i in range(x1,x2+1):
    for j in range(y1,y2+1):
        write(draw[i][j])
    line()
            
                
    
        
        
            