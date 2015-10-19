''''wrong'''
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

Point=namedtuple('point','x y')
 
def slope(p1,p2):
    if p2.x-p1.x==0:
        return Fraction(0,1)
    return Fraction((p2.y-p1.y),(p2.x-p1.x))
def get_slopes(p1,p2,p3):
    return slope(p1,p2),slope(p3,p1),slope(p2,p3)
def is_right(ps):
    m1,m2,m3=get_slopes(ps[0],ps[1],ps[2])
    slopes=[m1,m2,m3]
    for i in range(len(slopes)):
        for j in range(i+1,len(slopes)):
            if slopes[i].numerator==0:
                tmp=Fraction(0,1)
            else:
                tmp=Fraction(-slopes[i].denominator,slopes[i].numerator)
            if tmp==slopes[j]:
                return True
ps=read_integers()
p1=Point(ps[0],ps[1])
p2=Point(ps[2],ps[3])
p3=Point(ps[4],ps[5])
ps=[p1,p2,p3]
if is_right(ps):
    writeline("RIGHT") ; end()
dir=[(0,1),(1,0),(0,-1),(-1,0)]
for i,p in enumerate(ps):
    for d in dir:
        x=p.x+d[0]
        y=p.y+d[1]
    n_ps=list(ps)
    ps[i]=Point(x,y)
    if is_right(n_ps):
        writeline("ALMOST") ; end()
writeline("NEITHER")
        
        
        
    