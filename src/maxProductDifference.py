class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        a = nums[len(nums) - 1]
        b = nums[len(nums) - 2]
        c = nums[0]
        d = nums[1]
        return (a * b) - (c * d)