class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        nums.sort()
        evenNumbers: list[int] = []
        oddNumbers: list[int] = []
        for elm in nums:
            if elm % 2 == 0:
                evenNumbers.append(elm)
            else:
                oddNumbers.append(elm)
        return evenNumbers + oddNumbers

print(Solution.sortArrayByParity(object, [3,1,2,4]))