class Solution(object):
    def restoreString(self, s, indices):
        res  = ""
        dic = {}
        for i in range(0, len(indices)):
            dic[indices[i]] = s[i]
        for i in range (0, len(s)):
            res += dic[i]
        return res