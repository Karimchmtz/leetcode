class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for stone in stones:
            for letter in stone:
                if (letter in jewels):
                    count += 1
        return count
