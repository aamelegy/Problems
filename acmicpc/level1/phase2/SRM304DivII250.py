'''
Created on May 24, 2014

@author: sshadmin
'''
class RugSizes():
    def rugCount(self, area):
        count=0
        for i in range(1,area+1):
            if area % i !=0:
                continue
            j=area/i
            if i>j:
                break
            if (i%2!=0 or j%2!=0) or i==j:
                count+=1
        return count
                            