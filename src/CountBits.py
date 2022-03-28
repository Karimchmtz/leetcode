class Solution:

    def countBits(self, n: int) -> list[int]:

        def numberOfOnes(n: int) -> int:
            res = 0
            while (n > 0):
                if n % 2 == 1:
                    res += 1
                n = n // 2
            return res

        res = []

        for i in range(0, n + 1):
            res.append(numberOfOnes(i))
        return res
