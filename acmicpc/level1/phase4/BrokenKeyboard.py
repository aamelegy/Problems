#time limitss
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
    
def solve(word,m):
    s,cur,e,mx=0,0,0,0
    c=dict()
    for w in word:
        c[w]=0
    while True:    
        while e<len(word):
            if c[word[e]]==0 :
                if cur==m:
                    break
                cur+=1
            c[word[e]]+=1
            e+=1
        mx=max(mx,e-s)
        if e==len(word):
            return mx
        while cur==m:
            if c[word[s]]==1:
                cur-=1
            c[word[s]]-=1
            s+=1
while True:
    m=read_integer()
    if m==0:
        end()
    word=readline()
    print solve(word,m)
    