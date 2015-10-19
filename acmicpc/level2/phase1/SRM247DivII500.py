'''
Created on Jun 6, 2014

@author: sshadmin
'''
from fractions import gcd 
class FracCount():
    def position(self, numerator, denominator):
        c=0
        for i in range(2,1001):
            for j in range(i):
                if gcd(i,j)==1:
                    c+=1
                if i==denominator and j==numerator:
                    return c
                    
                    
                    
                    
                    
                    
            