class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        i = 0
        count = 0
        if (ruleKey == "type"):
            i = 0
        elif (ruleKey == "color"):
            i = 1
        elif (ruleKey == "name"):
            i = 2
        j = 0
        while (j < len(items)):
            s = items[j]
            if (s[i] == ruleValue):
                count += 1
            j += 1
        return count