class Solution(object):
    def maximum69Number (self, num):
        if (num > 1000):
            if (num < 9000):
                num += 3000
                return num
        if (num > 100):
            if (num < 900 or (num > 1000 and num - 9000 < 900)):
                num += 300
                return num
        if (num > 10):
            if (num < 90 or (num > 1000 and num - 9900 < 90) 
                or (num > 100 and num - 900 < 90)):
                num += 30
                return num
        if (num % 10 == 6):
            num += 3
            return num
        return num
