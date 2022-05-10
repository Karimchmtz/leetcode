class Solution:
    def sumZero(self, n: int) -> list[int]:
        result: list[int] = []
        if (n % 2 == 1):
            result.append(0)
            n -= 1
        k: int = 1
        while (n > 0):
            result.append(k)
            result.append(k * -1)
            n -= 2
            k += 1
        return result