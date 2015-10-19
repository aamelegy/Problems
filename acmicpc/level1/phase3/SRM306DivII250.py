'''
Created on May 30, 2014

@author: sshadmin
'''
class SortMachine():
    def countMoves(self, a):
        a,sa,p=list(a),sorted(a),0
        for i in range(len(a)):
            if a[i]==sa[p]:
                p+=1
        return len(a)-p

                