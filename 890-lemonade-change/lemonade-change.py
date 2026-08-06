class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five+=1
            elif i == 10:
                ten+=1
                if five:
                    five-=1
                else:
                    return False
            else:
                if ten!=0:
                    if ten:
                        ten-=1
                    else:
                        return False
                    if five: 
                        five-=1
                    else:
                        return False
                else:
                    if five>=3:
                        five-=3
                    else:
                        return False
        return True
        