class Solution(object):
    def nbDigits(self, number):
        if (number == 0):
            return 1
        count = 0
        while (number >= 0):
            if (number < 10):
                return count + 1
            if (number >= 10):
                number /= 10
                count += 1
        return count

    def findNumbers(self, nums):
        count = 0
        for n in nums:
            digits = Solution.nbDigits(self, n)
            if (digits % 2 == 0):
                count += 1
        return count