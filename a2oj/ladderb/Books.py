'''
Created on Sep 14, 2015

@author: sshadmin
'''
n,t=map(int,raw_input().strip().split())
a=map(int,raw_input().strip().split())
a=a
f,s,mx,sm=0,0,0,a[0]

while s<n:
    if sm<=t:
        mx=max(mx,s-f+1)
    if sm<t:
        s+=1
        if s<n:
            sm+=a[s]
    else:
        if f==s:
            f+=1
            s+=1
            if s<n:
                sm=a[f]
        else:
            sm-=a[f]
            f+=1
print mx
            
        
    
    
    
    
    