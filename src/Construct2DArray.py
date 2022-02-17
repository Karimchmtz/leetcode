class Solution(object):
    def construct2DArray(self, original, m, n):
        if (m * n != len(original)):
            return []
        tmp = []
        res = []
        for elm in original:
            tmp.append(elm)
            if (len(tmp) == n):
                res.append(tmp)
                tmp = []
        return res