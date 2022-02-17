class Solution(object):
    def replaceElements(self, arr):
        res = []
        l = len(arr)
        for i in range(0, l):
            arr.pop(0)
            if (len(arr) == 0):
                res.append(-1)
                break
            else:
                res.append(max(arr))
        return res