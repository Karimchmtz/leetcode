class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        buffer = []
        for letter in s:
            buffer.append(letter)
            if buffer.count('L') == buffer.count('R'):
                count += 1
                buffer.clear()
        return count