'''
Created on Jun 7, 2014

@author: sshadmin
'''

#wrong
class SpiralRoute():
    def thronePosition(self, width, length):
        sign=1
        x,y=0,length-1
        xc,yc=length-1,width-1
        mn=min(length,width)
        for i in reversed(range(1,mn)):
            y+=yc*sign
            sign= sign*-1
            y+=xc*sign
            yc-=1
            xc-=1
        return x,y
print SpiralRoute().thronePosition(6, 4)            
                
            
            
    