'''
Created on Jun 6, 2014

@author: sshadmin
'''
class KnightTour():
    def checkTour(self, cells):
        v=set()
        cells=list(cells)
        cells.append(cells[0])
        for i in range(len(cells)-1):
            xi=ord(cells[i][0])-64
            yi=int(cells[i][1])
            xi1=ord(cells[i+1][0])-64
            yi1=int(cells[i+1][1])
            if (xi,yi) in v :
                return "Invalid"
            else:
                v.add((xi,yi))
            if not((abs(xi-xi1)==1 and abs(yi-yi1)==2) or (abs(xi-xi1)==2 and abs(yi-yi1)==1)):
                return "Invalid"
        return "Valid"
