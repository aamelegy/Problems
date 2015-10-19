
#wrong
'''
Created on Jun 5, 2014

@author: sshadmin
'''
from math import *

class MinimalTriangle():
    def maximalArea(self, length):
        s=length*sin(radians(120))/sin(radians(30))
        a1=0.5*length*length*sin(radians(120))
        a2=0.5*length*s*sin(radians(90))
        return min(a1,a2)
