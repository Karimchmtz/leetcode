class Solution(object):
    def areOccurrencesEqual(self, s):
        dic = {}
        buff = ""
        for letter in s:
            if (not (letter in buff)):
                buff += letter
                dic[letter] = 1
            else:
                dic[letter] += 1
        count = None
        for key in dic:
            if (count == None):
                count = dic[key]
                continue
            else:
                if (count != dic[key]):
                    return False
        return True
