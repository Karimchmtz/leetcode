class Solution(object):
    def squareIsWhite(self, coordinates):
        num = int(coordinates[1])
        letter = coordinates[0]
        isNumEven = (num % 2 == 0)
        firstLetters = "aceg"
        secondLetters = "bdfh"
        if (isNumEven and (letter in firstLetters)):
            return True
        if (isNumEven and (letter in secondLetters)):
            return False
        if (not isNumEven and (letter in firstLetters)):
            return False
        return True