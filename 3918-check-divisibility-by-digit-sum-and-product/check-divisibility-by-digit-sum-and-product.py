class Solution:
    def checkDivisibility(self, n: int) -> bool:
        add=0
        mul=1
        for digit in str(n):
            add+=int(digit)
            mul*=int(digit)
        return n%(add+mul)==0