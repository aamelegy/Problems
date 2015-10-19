
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


def is_valid(num):
    if len(num)>1 and num[0]=='0' :
        return False
    elif int(num)>1000000:
        return False
    return True
    
max=0
valid=False
word=readline()
n=len(word)
for i in range(n-1):
    for j in range(i+1,n-1):
        first=word[0:i+1]
        second=word[i+1:j+1]
        third=word[j+1::]
        if is_valid(first) and is_valid(second) and is_valid(third):
            valid=True
            temp=int(first)+int(second)+int(third)
            if temp>max:
                max=temp
if not valid:
    writeline(-1)
else:
    writeline(max)
            
            
        