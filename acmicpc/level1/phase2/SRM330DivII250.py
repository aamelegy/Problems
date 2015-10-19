

class Sortness():
    def getSortness(self, a):
        n=len(a)
        su=0
        for i in range(n):
            for j in range(n):
                if j<i and a[j]>a[i]:
                    su+=1
                elif j>i and a[j]<a[i]:
                    su+=1
        return float(su)/float(n)
            
