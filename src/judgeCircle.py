class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for letter in moves:
            if letter == 'L':
                x -= 1
            elif letter == 'R':
                x += 1
            elif letter == 'U':
                y += 1
            elif letter == 'D':
                y -= 1
            print(x,y)
        return x == 0 and y == 0