'''
Created on May 31, 2014

@author: sshadmin
'''
#abnormal null  
class CandyShop():
    def countProbablePlaces(self, X, Y, R):
        X,Y,R,x=list(X),list(Y),list(R),[]
        for i in range(len(X)):
            p=[]
            for k in range(0,R[i]+1):
                for j in range(0,k+1):
                        p.append((X[i]+j,Y[i]+k-j))
                        p.append((X[i]-j,Y[i]-k+j))
                        p.append((X[i]+j,Y[i]-k+j))
                        p.append((X[i]-j,Y[i]+k-j))
            x.append(set(p))
            x=[set(reduce(lambda z,y:z&y,x))]
        return len(x[0])
        
            