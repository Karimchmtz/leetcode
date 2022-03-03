class Solution(object):
    def replaceDigits(self, s):
        res = ""
        for i in range (0, len(s)):
            x = None
            c = s[i]
            if (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9')):
                x = int(c)
                prevLetter = s[i - 1]
                c = chr(ord(prevLetter) + x)
            res += c
        return res
