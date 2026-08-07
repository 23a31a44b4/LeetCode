class Solution(object):
    def solveNQueens(self, n):
        res=[]
        board=[['.']*n for _ in range(n)]
        def is_safe(row,col):
            #upper
            for r in range(row-1,-1,-1):
                if board[r][col]=='Q':
                    return False
            #left diagonal
            r = row-1
            c = col-1
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            #right diagonal
            r = row-1
            c = col+1
            while r>=0 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            return True


        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in  board])
                return
            for col in range(n):
                if is_safe(row,col):
                    board[row][col]='Q'
                    backtrack(row+1)
                    board[row][col]='.'


        backtrack(0)
        return res