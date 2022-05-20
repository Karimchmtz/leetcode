class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for i in range(0, len(nums), 2):
            tmp = min(nums[i], nums[i + 1])
            res += tmp
        return res