class Solution(object):
    def findTheDifference(self, s, t):
        a = 0
        b = 0
        for letter in s:
            a += ord(letter)
        for letter in t:
            b += ord(letter)
        return chr(b - a)