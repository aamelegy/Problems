#wrong
from __future__ import division
import itertools ; import math

from bisect import bisect_left,bisect_right
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def pre(n):
    x=list(itertools.takewhile(lambda p: p<n, erat2()))
    return x

def bisect(x,lo,hi):
    s=bisect_left(x,lo)
    e=bisect_right(x,hi)
    return x[s:e]
   
def solve(a,b,p):
    pri=bisect(primes,p,b-a)
    prime_set=set(pri)
    prime_dic=dict()
    prime_graph=dict()
    counted=set([])
    for p in pri:
        if p not in prime_graph:
                    prime_graph[p]=set()
        start=int(math.ceil(a/p)) ; end=int(b/p)
        if p not in prime_dic:
            prime_dic[p]=0
        for i in range(start,end+1):
            if i*p not in counted:
                prime_dic[p]+=1
                counted.add(i*p)
            if i in prime_set:
                if i not in prime_graph:
                    prime_graph[i]=set()
                if p<i:
                    prime_graph[p].add(i)
                else:
                    prime_graph[i].add(p)
    sets=[]
    for p in prime_graph.keys():
        set_found=False
        for se in sets:
            if any(value for value in prime_graph[p] if value in se) or p in se:
                set_found=True
                for op in prime_graph[p]:
                    se.add(op)
                break
        if not set_found:
            sets.append(set([p]+list(prime_graph[p])))
    return b-a+1-sum(prime_dic.values())+len(sets)
        
primes=pre(10**4)
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip().split(' ')
    a=int(line[0]) ; b=int(line[1]) ; p =int(line[2])
    fout.write("Case #"+str(case)+": "+str(solve(a,b,p))+"\n")