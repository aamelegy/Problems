'''
Created on May 31, 2014

@author: sshadmin
'''
class MultiNumber():
    def check(self, number):
        word=str(number)
        for i in range(1,len(word)):
            n1=word[0:i]
            n2=word[i::]
            n1=int(reduce(lambda x,y:int(x)*int(y),n1))
            n2=int(reduce(lambda x,y:int(x)*int(y),n2))
            if n1==n2:
                return "YES"
        return "NO"
    
