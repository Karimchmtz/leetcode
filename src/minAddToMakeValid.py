class Solution(object):
    def minAddToMakeValid(self, s):
        buffer = []
        for letter in s:
            if letter == '(':
                buffer.append(letter)
            else:
                if (len(buffer) > 0 and buffer[len(buffer) - 1] == '('):
                    buffer.pop()
                else:
                    buffer.append(letter)
        return len(buffer)