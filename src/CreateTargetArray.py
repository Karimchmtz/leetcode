class Solution(object):
    def createTargetArray(self, nums, index):
        l = []
        for i in range(0, len(nums)):
            n = nums[i]
            target = index[i]
            l.insert(target, n)
        return l