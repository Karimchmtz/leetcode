class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 0: 
            return ""
        res = ""
        if (n % 2 == 0):
            res += 'a'
            n -= 1
        if n > 0:
            res += 'z' * n
        return res