class Solution(object):
    def decompressRLElist(self, nums):
        res = []
        count = None
        first = True
        for i in nums:
            if (first == True):
                count = i
                first = False
                continue
            else:
                for j in range (0, count):
                    res.append(i)
                first = True
                count = None
                continue
        return res 