class Solution:
    def countPrefixes(self, words: list, s: str) -> int:
        def isPrefix(prefix: str, word: str) -> bool:
            i = 0
            for letter in prefix:
                if i == len(word):
                    return False
                if letter != word[i]:
                    return False
                i += 1
            return True
        count = 0 

        for pre in words:
            if isPrefix(pre, s):
                count += 1

        return count
        