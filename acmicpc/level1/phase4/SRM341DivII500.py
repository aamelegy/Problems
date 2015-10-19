'''
Created on Jun 4, 2014

@author: sshadmin
'''

class KLastNonZeroDigits():
    def getKDigits(self, N, K):
        f=N
        for i in reversed(range(1,N)):
            f*=i
        word=str(f)
        e=len(word)-1
        while (word[e]=='0'):
            e-=1
        s=max(0,e-K+1)
        return word[s:e+1]