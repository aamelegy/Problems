'''
Created on Sep 12, 2015

@author: sshadmin
'''
n=input()
h=[]
for i in range(n):
    h.append(input())
t,hi=h[0]+1,h[0]
for i in range(1,n):
    if hi>h[i]:
        t+=hi-h[i]
        hi=h[i]
        t+=2
    else:
        t+=1
        t+=h[i]-hi
        t+=1
        hi=h[i]
print t
    

    