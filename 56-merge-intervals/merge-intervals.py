class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort()
            res=[intervals[0]]
            for st,end in intervals[1:]:
                if st <= res[-1][1]:
                    res[-1][1]=max(end,res[-1][1])
                else:
                    res.append([st,end])
            return res 
