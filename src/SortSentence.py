class Solution(object):
    def sortSentence(self, s):
        res = ""
        dic = {}
        buffer = ""
        keys = []
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        i = 0
        while (i < len(s)):
            c = s[i]
            if (c == ' '):
                i += 1
            elif (c in numbers):
                dic[int(c)] = buffer
                buffer = ""
                i += 1
                keys.append(int(c))
            else:
                buffer += c
                i += 1
        keys.sort()
        i = 0
        while (i < len(keys)):
            res += dic[keys[i]]
            if (i != len(keys) - 1):
                res += ' '
            i += 1
        return res