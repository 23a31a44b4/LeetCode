class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original=image[sr][sc]
        row,col=len(image),len(image[0])
        if image[sr][sc]==color:
            return image
        def backtrack(r,c):
            if r<0 or c<0 or r>=row or c >=col or image[r][c]!=original:
                return
            image[r][c]=color
            backtrack(r-1,c)
            backtrack(r,c-1)
            backtrack(r+1,c)
            backtrack(r,c+1)
        backtrack(sr,sc)
        return image