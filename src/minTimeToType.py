class Solution:
    def minTimeToType(self, word: str) -> int:

        def difference(a: int, b: int) -> int: 
            x = (a - b) % 26
            return x

        seconds = 0
        start = ord('a')
        for letter in word:
            letterNumber = ord(letter)
            diff = min(difference(start, letterNumber), difference(letterNumber, start))
            start = letterNumber
            seconds += 1
            seconds += diff
        return seconds 