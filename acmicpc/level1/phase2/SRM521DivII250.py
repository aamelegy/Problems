


class RedAndGreen():
    def minPaints(self, row):
        r=row.count('R')
        g=len(row)-r
        mn=min(g,r)
        g=0
        for i in range(len(row)):
            if row[i]=='G':
                g+=1
            elif row[i]=='R':
                r-=1
            mn=min(g+r,mn)
        return mn
    
    
#slower
# class RedAndGreen():
#     def minPaints(self, row):
#         mn=float('inf')
#         for i in range(len(row)+1):
#             mn=min(row[0:i].count("G")+row[i::].count("R"),mn)
#         return mn
            
                
            