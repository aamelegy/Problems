'''
Created on Sep 14, 2015

@author: sshadmin
'''
import sys
n,m=map(int,raw_input().strip().split())
if m==0:
    print "YES"
    sys.exit()
d=map(int,raw_input().strip().split())

d.sort()
if m==0:
    print "YES"
elif d[0]==1 or d[-1]==n:
    print "NO"
elif m<=2:
    print "YES"
else:
    f=d[0]
    s=d[1]
    for i in range(2,m):
        if d[i]-s==1 and s-f==1:
            print "NO"
            sys.exit()
        else:
            s=d[i]
            f=d[i-1]
    print "YES"
            
            
        
        
        
        
    