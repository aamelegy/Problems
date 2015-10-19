'''
Created on Jun 4, 2014

@author: sshadmin
'''
class VacationTime():
    def bestSchedule(self, N, K, workingDays):
        mn=float('inf')
        days=set(workingDays)
        c=0
        for j in range(1,K+1):
            if j in days:
                c+=1
        mn=min(mn,c)
        for i in range(2,N-K+2):
            if i-1 in days:
                c-=1
            if i+K-1 in days:
                c+=1
            mn=min(mn,c)
        return mn
                
'''
correct also
class VacationTime():
    def bestSchedule(self, N, K, workingDays):
        mn=float('inf')
        days=set(workingDays)
        for i in range(1,N-K+2):
            c=0
            for j in range(i,K+i):
                if j in days:
                    c+=1
            mn=min(mn,c)
        return mn
'''               
                