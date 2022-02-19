class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        i = 0
        for letter in word1:
            count1 = word1.count(letter)
            count2 = word2.count(letter)
            difference = count1 - count2
            if (difference > 3):
                return False
            if (difference < -3):
                return False
            letter2 = word2[i]
            count_1 = word1.count(letter2)
            count_2 = word2.count(letter2)
            difference = count_1 - count_2
            if (difference > 3):
                return False
            if (difference < -3):
                return False
            i += 1
        return True