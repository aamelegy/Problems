'''
Created on May 30, 2014

@author: sshadmin
'''

class Highscore():
    def getRank(self, scores, newscore, places):
        r=1
        p=0
        if len(scores)==0:
            return 1
        while p<places:
            if p==len(scores) or scores[p]<newscore :
                if newscore!=scores[p-1]:
                    r=p+1
                return r
            else:
                if scores[p]!=scores[p-1]:
                    r=p+1
            p+=1
        return -1