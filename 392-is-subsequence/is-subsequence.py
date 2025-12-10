class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                idx=t.index(s[i])
                t=t[idx+1:]
            else:
                return False
        return True
        