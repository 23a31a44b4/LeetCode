class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        while n!=1 and n not in visited:
            sum=0
            visited.add(n)
            for i in str(n):
                sum+=int(i)**2
            n=sum
        return n==1