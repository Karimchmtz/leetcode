class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        cmp = 0
        copy = x
        while ( x > 0):
            if (x >= 10):
                cmp += x  % 10
                x = x // 10
                cmp *= 10
            else:
                cmp += x
                x = 0
        return cmp == copy
                