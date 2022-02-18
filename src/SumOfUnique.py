class Solution(object):
    def sumOfUnique(self, nums):
        res = 0
        for i in range (0, len(nums)):
            count = nums.count(nums[i])
            if (count == 1):
                res += nums[i]
        return res