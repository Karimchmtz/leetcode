class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        start = ord('a')
        end = ord('z') + 1
        for i in range(start, end):
            letter = chr(i)
            if not letter in sentence:
                return False
        return True