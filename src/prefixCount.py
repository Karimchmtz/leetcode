class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        def isPrefixOfWord(prefix: str, word: str) -> bool:
            if len(prefix) == 0:
                return True
            i = 0
            if word == prefix: 
                return True
            for letter in word:
                if i >= len(prefix):
                    return True
                if letter != prefix[i]:
                    break
                i += 1
            return False

        count = 0 
        for word in words:
            if isPrefixOfWord(pref, word):
                count += 1
        return count