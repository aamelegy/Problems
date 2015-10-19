'''
Created on May 31, 2014

@author: sshadmin
'''
class FarFromPrimes():
    def is_prime(self,n):
        x=int(n**0.5+2)
        if n==0 or n==1:
            return False
        for i in range(2,x):
            if n%i==0:
                return False
        return True
            
    def count(self, A, B):
        c=0
        prime=[A-11,B+11]
        for i in range(A-10,B+11):
            if self.is_prime(i):
                prime.append(i)
        prime.sort()
        for i in range(1,len(prime)):
            c+=max(0,prime[i]-10-(prime[i-1]+11))
        return c
    