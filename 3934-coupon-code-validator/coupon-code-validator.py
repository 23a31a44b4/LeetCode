class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid=[]
        business=set({"electronics", "grocery", "pharmacy", "restaurant"})
        for i in range(len(code)):
            if code[i]!="" and re.fullmatch(r"[a-zA-Z0-9_]+",code[i]) and isActive[i] and businessLine[i]in business :
                valid.append((businessLine[i],code[i]))
        valid.sort()
        return [i for _,i in valid]