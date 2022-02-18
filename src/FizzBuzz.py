class Solution(object):
    def fizzBuzz(self, n):
        res = []
        k = 1
        for i in range (0, n):
            if (k % 3 == 0 and k % 5 == 0):
                res.append("FizzBuzz")
                k += 1
                continue
            if (k % 3 == 0):
                res.append("Fizz")
                k += 1
                continue
            if (k % 5 == 0):
                res.append("Buzz")
                k += 1
                continue
            res.append(str(k))
            k += 1
        return res