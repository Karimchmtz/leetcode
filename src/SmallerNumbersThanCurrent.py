class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if (nums[j] < nums[i]):
                    count[i] += 1
        return count