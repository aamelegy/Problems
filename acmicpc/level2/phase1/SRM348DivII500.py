'''
Created on Jun 5, 2014

@author: sshadmin
'''
import re
class LostParentheses():
    def minResult(self, e):
        e=e.replace('+',' + ')
        e=e.replace('-',' - ')
        tokens=e.split(' ')
        sm=0
        add=lambda x,y:x+y
        sub=lambda x,y:x-y
        op=add
        for t in tokens:
            if t=='-':
                op=sub
            elif t=="+":
                continue
            else:
                sm=op(sm,int(t))
        return sm
                
