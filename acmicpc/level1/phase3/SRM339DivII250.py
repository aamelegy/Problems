'''
Created on May 30, 2014

@author: sshadmin
'''
class BettingStrategy():
    def finalSum(self, initSum, outcome):
        bet=1
        for b in outcome:
            if bet>initSum:
                return initSum
            if b=='W':
                initSum+=bet
                bet=1
            else:
                initSum-=bet
                bet*=2
        return initSum