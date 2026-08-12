class Solution(object):
    def tribonacci(self, n):
        if n<2:
            return n
        if n ==2:
            return 1
        f1 = 0
        f2 = 1
        f3 = 1
        for _ in range(3,n+1):
            res = f1+f2+f3
            f1 = f2
            f2 = f3
            f3 = res
        return res
        