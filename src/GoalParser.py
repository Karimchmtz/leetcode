class Solution(object):
    def interpret(self, command):
        res = ""
        i = 0
        while (i < len(command)):
            c = command[i]
            if (c == 'G'):
                res += 'G'
                i += 1
            elif (c == '(' and command[i + 1] == ')'):
                res += 'o'
                i += 2
            else:
                res += 'al'
                i += 4
        return res