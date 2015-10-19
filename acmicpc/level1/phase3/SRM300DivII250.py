'''
Created on May 30, 2014

@author: sshadmin
'''
from math import sqrt
class Taxi():
    def maxDis(self, maxX, maxY, taxiDis):
        mx=max(maxX,maxY)
        if maxX+maxY<taxiDis:
            return -1
        elif taxiDis<=mx:
            return taxiDis
        else:
            return sqrt((taxiDis-mx)**2+mx**2)