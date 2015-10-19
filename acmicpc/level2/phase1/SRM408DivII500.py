'''
Created on Jun 6, 2014

@author: sshadmin
'''

class OlympicCandles():
    def numberOfNights(self, candles):
        n=1
        candles=list(candles)
        while True:
            candles.sort(reverse=True)
            for i in range(n):
                if i==len(candles) or candles[i]==0:
                    return n-1
                else:
                    candles[i]-=1
            n+=1
            