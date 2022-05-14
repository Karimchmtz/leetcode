class Solution:
    def largestGoodInteger(self, num: str) -> str:
        def find_max(l: list) -> int:
            res = 0
            for i in range(0, len(l)):
                if int(l[i]) > int(l[res]):
                    res = i
            return res
        def returnGoodIntegrs(num: str) -> list:
            res = []
            if len(num) < 3:
                return res

            for i in range(0, len(num)):
                if len(num) - i < 3:
                    return res
                if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                    buffer: str = "" + num[i] + num[i] + num[i]
                    res.append(buffer)
            return res
        goodIntegers = returnGoodIntegrs(num)
        if len(goodIntegers) == 0:
            return ""
        return goodIntegers[find_max(goodIntegers)]