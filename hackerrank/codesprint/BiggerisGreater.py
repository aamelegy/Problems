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


def nextp(w):
    k=-1
    for i in range(len(w)-2,-1,-1):
        if w[i]<w[i+1]:
            k=i
            break
    if k == -1:
        print "no answer"
        return False
    l=-1
    for j in range(len(w)-1,-1,-1):
        if w[j]>w[k]:
            l=j
            break
    tmp=w[i]
    w[i]=w[l]
    w[l]=tmp
    w[i+1:] = reversed(w[i+1:])   
    print "".join(w) 
    return
t=read_integer()
for _ in range(t):
    w=list(readline())
    nextp(w)
    
                    
            
        
        
        
        
        

