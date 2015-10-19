

class GridGenerator():
    def generate(self, row, col):
        a=[]
        for i in range(len(col)):
            a.append([0]*len(row))
        for i in range(len(row)):
            a[0][i]=row[i]
        for i in range(len(col)):
            a[i][0]=col[i]
        for i in range(1,len(row)):
            for j in range(1,len(col)):
                a[i][j]=a[i][j-1]+a[i-1][j]+a[i-1][j-1]
        return a[len(row)-1][len(col)-1]
    
