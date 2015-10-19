'''
Created on May 30, 2014

@author: sshadmin
'''
#notyet
from fractions import gcd

class DreamingAboutCarrots():
        def carrotsBetweenCarrots(self, x1, y1, x2, y2):
            xt2,xt1,yt1,yt2=max(x1,x2),min(x1,x2),min(y1,y2),max(y1,y2),
            x2,x1,y1,y2=xt2,xt1,yt1,yt2
            slopey=y2-y1
            slopex=x2-x1
            g=gcd(slopey,slopex)
            slopey/=g
            slopex/=g
            p=0
            for i in range(x1+1,x2):
                if i%slopex==0:
                    p+=1
            return p
                
            
print DreamingAboutCarrots().carrotsBetweenCarrots(42,0, 0, 0)             
                
            