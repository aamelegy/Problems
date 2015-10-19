'''
Created on Sep 13, 2015

@author: sshadmin
'''
x,a,b=map(int,raw_input().strip().split())
c,y,d=map(int,raw_input().strip().split())
e,f,z=map(int,raw_input().strip().split())

for i in range(100001):
    x=i
    sm=x+a+b
    y=sm-c-d
    z=sm-e-f
    if x+c+e==sm:
        if y+a+f==sm:
            if b+d+z==sm:
                if x+y+z==sm:
                    if y+e+b==sm:
                        print x,a,b
                        print c,y,d
                        print e,f,z
