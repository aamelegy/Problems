'''
Created on Sep 14, 2015

@author: sshadmin
'''
m,n=map(int,raw_input().strip().split())

import sys
grid=[]
for i in range(m):
    grid.append(map(int,raw_input().strip().split()))
r,c=set([]),set([])
for i in range(m):
    if all([True if grid[i][x] ==1 else 0 for x in range(n)]):
        r.add(i)
for i in range(n):
    if all([True if grid[x][i] ==1 else 0 for x in range(m)]):
        c.add(i)   
if sum([sum(grid[x]) for x in range(m)])==0:
    print "YES"
    for i in range(m):
        print " ".join(["0"]*n)
elif len(r) ==0 or len(c)==0:
    print "NO"
else:
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and i not in r and j not in c:
                print "NO"
                sys.exit()
    rgrid=[]
    for i in range(m):
        rgrid.append([0]*n)
    r,c=list(r),list(c)
    for i in range(len(r)):
        for j in range(len(c)):
            rgrid[r[i]][c[j]]=1
    print "YES"
    for i in range(m):
        print " ".join(map(str,rgrid[i]))
            
        
        
     
        