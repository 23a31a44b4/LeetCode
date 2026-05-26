class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n=len(s)
        if s[n-1]=='1':
            return False
        visited=[False]*n
        visited[0]=True
        moved=0
        for j in range(1,n):
            if s[j]>=minJump and visited[j-minJump]:
                moved+=1
            if s[j]>maxJump and visited[j-maxJump-1]:
                moved-=1
            if moved>0 and s[j]=='0':
                visited[j]=True
        return visited[n-1]
        