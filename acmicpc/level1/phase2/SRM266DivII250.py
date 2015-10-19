'''
Created on May 24, 2014

@author: sshadmin
'''
import math
class SwimmersDelight():
    def dist(self,x1,y1,x2,y2):
        return math.sqrt((x1 - x2) * (x1 - x2)  +  (y1 - y2) * (y1 - y2))
    def longestJump(self,x,y):
        d1=self.dist(0,y[0],x[0],y[0])
        d2=self.dist(0,y[1],x[1],y[1])
        d3=self.dist(x[0],y[0],10,y[0])
        d4=self.dist(x[1],y[1],10,y[1])
        d5=abs(self.dist(x[0],y[0],x[1],y[1]))
        mn=min(max(d1,d3),max(d2,d4),max(d1,d5,d4),max(d5,d2,d3))
        return round(mn)
        
        