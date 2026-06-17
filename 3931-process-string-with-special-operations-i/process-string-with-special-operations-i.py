class Solution(object):
    def processStr(self, s):
        res=[]
        for ch in s:
            if ch=="#":
                res.extend(res)
            elif ch=="*":
                if res:
                    res.pop()
            elif ch=="%":
                res.reverse()
            else:
                res.append(ch)
        return "".join(map(str,res))