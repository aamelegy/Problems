from __future__ import division
import sys
from collections import namedtuple #x=namedtuple('point','x y')
from math import *
from collections import deque, OrderedDict #append #popleft
from fractions import gcd
from copy import copy ,deepcopy
from collections import Counter #Counter(list)
import re #re.split("[^a-zA-Z]",text)
from decimal import Decimal
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
def end():
    sys.exit()
def readbig():
    return [Decimal(x) for x in fin.readline().strip().split(' ')]
n,m=read_integers()
grid=[]
for i in range(n):
    grid.append(list(readline()))
dir=[(0,1),(1,0),(0,-1),(-1,0)]
r=0
rlast=-1
while rlast!=r:
    rlast=r
    for i in range(n):
        for j in range(m):
            p,px,py,wx,wy=0,0,0,i,j
            if grid[i][j]=="P":
                for d in dir:
                    if d[0]+i<n and d[0]+i>=0 and d[1]+j >=0 and d[1]+j <m:
                        x=d[0]+i 
                        y=d[1]+j
                        if grid[x][y]=='W':
                            p+=1
                            px=x
                            py=y
                if p==1:
                    grid[px][py]="."
                    grid[wx][wy]="."
                    r+=1
                    
print r            