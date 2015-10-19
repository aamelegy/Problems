'''
        Created on Nov 30, 2013
        
        @author: sshadmin
        '''
        #incorrect
def rec(p,d,i,m,f):
    if len(p)==0:
        return 0
    best=rec(p[1::],d,i,m,f)+d
    for j in range(256):
        move_cost = abs(j - p[0])
        if m==0 and move_cost!=0:
            return 999999999
        if m!=0:
            insert_cost = max(((abs(f - j)-1 ) / m)*i,0)
        else:
            insert_cost=0
        value=rec(p[1::],d,i,m,j)
        best=min(value+move_cost+insert_cost,best)
    return best
    
def solve(p,d,i,m,n):
    best=999999
    for j in range(256):
        move_cost = abs(j - p[0])
        value=rec(p[1::],d,i,m,j)
        best=min(value+move_cost,best)
    return best
fin=open('../in','r') ; fout=open('../out','w')
cases=int(fin.readline().strip())
for case in range(1,cases+1):
    print case
    l=[int(x) for x in fin.readline().strip().split(' ')]
    d=l[0];i=l[1];m=l[2];n=l[3]
    p=[int(x) for x in fin.readline().strip().split(' ')]
    fout.write("Case #"+str(case)+": "+str(solve(p,d,i,m,n))+"\n")