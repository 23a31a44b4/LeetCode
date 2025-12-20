class Solution(object):
    def minDeletionSize(self, strs):
        res=["".join(chars) for chars in zip(*strs)]
        count=0
        for i in res:
            if list(i)!=sorted(i):
                count+=1
        return count
        