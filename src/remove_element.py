class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        j = len(nums)
        i = 0
        while (i < j):
            if (nums[i] == val):
                nums.pop(i)
                k -= 1
                j = len(nums)
            else:
                i += 1
        return k