'''
Created on May 30, 2014

@author: sshadmin
'''
class Chessboard():
    def changeNotation(self, cell):
        if not cell[0].isalpha():
            x,y=divmod(int(cell)-1,8)
            return chr(ord('a')+y)+str(x+1)
        else:
            return str(ord(cell[0])-96+(int(cell[1])-1)*8)