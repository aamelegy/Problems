#small
from __future__ import division
from copy import copy

def suffice(nvs,d,t):
    vs=copy(nvs)
    vs[0]-=t
    for i in range(1,len(vs)):
        if vs[i]-vs[i-1]>d:
            vs[i]-=min(vs[i]-vs[i-1]-d,t,t)
        elif vs[i]-vs[i-1]<d:
            if t>=-vs[i]+vs[i-1]+d:
                vs[i]+=-vs[i]+vs[i-1]+d
            else:
                return False
    return True
    
def solve (vs,d):
    lower_bound = 0
    upper_bound = 10**12
    while upper_bound - lower_bound > (10**-8) * upper_bound :
        t = (lower_bound + upper_bound) / 2
        if suffice(vs,d,t):
            upper_bound = t
        else:
            lower_bound = t
    return lower_bound
        
        
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    line=fin.readline().strip().split(' ')
    d=int(line[1]) ; c =int(line[0])
    vs=[]
    for i in range(c):
        line=[int(x) for x in fin.readline().strip().split(' ')]
        for j in range(line[1]):
            vs.append(line[0])
    fout.write("Case #"+str(case)+": "+str(solve(vs,d))+"\n")