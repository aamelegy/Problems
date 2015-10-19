'''
Created on May 21, 2014

@author: sshadmin
'''

class DiagonalDisproportion():
    def getDisproportion(self, matrix):
        sum=0
        n=len(matrix)
        for i in range(n):
            sum+=int(matrix[i][i])
            sum-=int(matrix[i][n-i-1])
        return sum
            
        