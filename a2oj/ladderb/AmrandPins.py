'''
Created on Sep 12, 2015

@author: sshadmin
'''
from math import ceil
r,x,y,xd,yd=map(int,raw_input().strip().split())

d=((yd-y)**2 +(xd-x)**2)**0.5

print int(ceil(d/(2*r)))