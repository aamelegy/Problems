

class TheSquareDivTwo():
    def solve(self, board):
        r=[]
        l=len(board)
        n_board=[]
        for i in range(l):
            r.append(board[i].count('C'))
            n_board.append(["."]*l)
        for i in range(l-1,-1,-1):
            for j in range(l):
                if r[j]>0:
                    n_board[i][j]='C'
                    r[j]-=1
        for i in range(l):
            n_board[i]=''.join(n_board[i])
        return n_board
