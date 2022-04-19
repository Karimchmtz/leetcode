class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        def rec(num1, num2, count):
            if num1 == 0:
                return count
            if num2 == 0:
                return count 
            if num1 > num2:
                return rec(num1 - num2, num2, count + 1)
            return rec(num2 - num1, num1, count + 1)
            
        return rec(num1, num2, count)