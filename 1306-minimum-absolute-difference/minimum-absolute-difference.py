class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        diff=float('inf')
        for i in range(len(arr)-1):
            diff=min(diff,arr[i+1]-arr[i])
        print(diff)
        res=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==diff:
                res.append([arr[i-1],arr[i]])
        return res
        