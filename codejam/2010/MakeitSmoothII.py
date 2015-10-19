'''
Created on Nov 30, 2013

@author: sshadmin
'''
def solve(p,final):
    n=len(p)
    if n==0:
        return 0
    best=solve(p[0:n-1],p[n-1])+d
    for i in range(0,256):
        move_cost=abs(final-p[n-1])
        num_inserts = (abs(final - i) - 1) / m
        insert_cost = num_inserts * i
        cost=solve(p[0:n-1],i)
        best=min(best,cost+insert_cost+move_cost)
    return best

fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
d=0;i=0;m=0;n=0
for case in range(1,cases+1):
    print case
    l=[int(x) for x in fin.readline().strip().split(' ')]
    d=l[0];i=l[1];m=l[2];n=l[3]
    p=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(p[0:n-1],p[n-1]))+"\n")