'''
Created on Sep 12, 2015

@author: sshadmin
'''
n=input()
a=map(int,raw_input().strip().split())
if len(a)==1 :
    print 0
elif len(a)==2:
    if a[0] > a[1]:
        print 1
    else:
        print 0
else:
    i=1
    while i < len(a) and a[i] >= a[i-1]:
        i+=1
    if i==len(a):
        print 0
    else:
        if a[i::]==sorted(a[i::]) and a[-1]<= a[0]:
            print len(a)-i
        else:
            print -1
    
    