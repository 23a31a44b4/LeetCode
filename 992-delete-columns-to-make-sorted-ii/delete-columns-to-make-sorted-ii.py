class Solution(object):
    def minDeletionSize(self, strs):
        n=len(strs)
        m=len(strs[0])
        count=0
        resolved=[False]*(n-1)
        for col in range(m):
            violation=False
            for i in range(n-1):
                if resolved[i]:
                    continue
                if strs[i][col]>strs[i+1][col]:
                    violation=True
                    break
            if violation:
                count+=1
                continue
            for i in range(n - 1):
                if not resolved[i] and strs[i][col] < strs[i + 1][col]:
                    resolved[i] = True

            if all(resolved):
                break
        return count
                
        
        