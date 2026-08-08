class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row , col = len(grid),len(grid[0])
        count=0
        def backtrack(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] =='0':
                return 
            grid[r][c]='0'
            backtrack(r+1,c)
            backtrack(r-1,c)
            backtrack(r,c-1)
            backtrack(r,c+1)
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] =='1':
                    backtrack(r,c)
                    count+=1
        return count