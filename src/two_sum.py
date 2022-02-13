class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range (0, len(nums)):
            for j in range (i + 1, len(nums)):
                if i != j:
                    if (nums[i] + nums[j] == target):
                        result.append(i)
                        result.append(j)
                        return result
        return result