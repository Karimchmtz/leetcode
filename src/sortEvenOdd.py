class Solution:
    def sortEvenOdd(self, nums: list) -> list:
        oddValues = []
        evenValues = []
        for i in range(1, len(nums), 2):
            oddValues.append(nums[i])
        for j in range(0, len(nums), 2):
            evenValues.append(nums[j])
        evenValues.sort()
        oddValues.sort()
        i = 0
        j = len(oddValues) - 1
        res = []
        while (j > -1 or i < len(evenValues)):
            if (i < len(evenValues)):
                res.append(evenValues[i])
                i += 1
            if (j > -1):
                res.append(oddValues[j])
                j -= 1
        return res