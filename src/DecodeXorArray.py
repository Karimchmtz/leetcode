class Solution(object):
    def decode(self, encoded, first):
        res = [first]
        for elm in encoded:
            a = res[len(res) - 1]
            res.append(a ^ elm)
        return res