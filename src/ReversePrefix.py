class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.count(ch) == 0:
            return word
        res = ""
        pre = ""
        chEncountered = False
        for letter in word:
            if not chEncountered and letter == ch:
                chEncountered = True
                pre = letter + pre
                res = res + pre
                continue
            elif not chEncountered:
                pre = letter + pre
                continue
            else:
                res += letter
        return res