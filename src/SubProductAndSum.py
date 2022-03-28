class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        def getdigits(n: int) -> list[int]:
            if (n == 0):
                return [0]
            res = []
            while(n >= 10):
                nextDigit = n % 10
                n = n // 10
                res.append(nextDigit)
            res.append(n)
            return res 
        
        digits = getdigits(n)
        product, summ = 1, 0
        for elm in digits:
            product *= elm
            summ += elm
        
        return product - summ