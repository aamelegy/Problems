

class WhiteCells():
    def even(self,x):
        if x%2==0:
            return True
    def countOccupied(self, board):
        count=0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (self.even(i) and self.even(j)) or (not self.even(i) and not self.even(j)):
                    if board[i][j]=="F":
                        count+=1
        return count
                    
                
        