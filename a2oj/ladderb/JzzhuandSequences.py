'''
Created on Sep 12, 2015

@author: sshadmin
'''

x,y=map(int,raw_input().strip().split())
n=input()

z=y-x
r=[x,y,z,-x,-y,-z]
n= n % 6
print r[n-1] % 1000000007

        
    