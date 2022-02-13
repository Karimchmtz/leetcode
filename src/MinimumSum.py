class Solution(object):
    def minimumSum(self, num):
        num = sorted(list(map(int, str(num))))
        return (10 * num[0] + num[2]) + (10 * num[1] + num[3])