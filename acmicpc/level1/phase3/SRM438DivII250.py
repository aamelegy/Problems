'''
Created on May 30, 2014

@author: sshadmin
'''
class UnluckyNumbers():
    def getCount(self, luckySet, n):
        ls=list(luckySet)
        ls.append(0)
        ls=sorted(ls)
        a,b=0,0
        for i in range(len(ls)):
            if ls[i]==n:
                return 0
            elif ls[i]>n:
                a=ls[i]
                b=ls[i-1]
                break
        return (n-b-1)*(a-n)+(a-n-1)
        
