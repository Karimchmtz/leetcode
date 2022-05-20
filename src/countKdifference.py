class Solution:
    def countKDifference(self, nums: list, k: int) -> int:
        def difference(a, b) -> int:
            if a > b:
                return a - b
            return b - a
        count = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if difference(nums[i], nums[j]) == k:
                    count += 1
        return count