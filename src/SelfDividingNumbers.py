class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def getDigits(number: int) -> list[int]:
            res: list[int] = []
            while number >= 10:
                res.append(number % 10)
                number = number // 10
            if number > 0:
                res.append(number)
            res.reverse()
            return res
        res = []
        for i in range(left, right + 1):
            digitsOfNumber: list[int] = getDigits(i)
            isSelfDividing = True
            if 0 in digitsOfNumber:
                continue
            for d in digitsOfNumber:
                if i % d != 0:
                    isSelfDividing = False
            if isSelfDividing:
                res.append(i)
        return res