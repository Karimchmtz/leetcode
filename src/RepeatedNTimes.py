class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        for j in nums:
            if (nums.count(j) == n):
                return j
        return None