'''
Created on May 31, 2014

@author: sshadmin
'''
class CucumberMarket():
    def check(self, price, budget, k):
        price=sorted(price,reverse=True)
        if sum(price[0:k])<=budget:
            return "YES"
        return "NO"