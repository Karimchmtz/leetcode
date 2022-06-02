class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigits(n: int) -> list:
            res = []
            while (n >= 10):
                res.append(n % 10)
                n //= 10
            res.append(n)
            return res
        if (n == 1):
            return True
        l = []
        while n not in l and n != 1:
            l.append(n)
            n = sum(list(map(lambda x: x * x ,getDigits(n))))
            if (n == 1):
                return True
        return False