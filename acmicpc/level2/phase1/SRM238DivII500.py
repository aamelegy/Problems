'''
Created on Jun 7, 2014

@author: sshadmin
'''

class PrintScheduler():
    def getOutput(self, threads, slices):
        p=[0]*len(threads)
        r=[]
        for slice in slices:
            x=slice.split(' ')
            for i in range(int(x[1])):
                j=p[int(x[0])]%len(threads[int(x[0])])
                r.append(threads[int(x[0])][j])
                p[int(x[0])]+=1
        return ''.join(r)
        
