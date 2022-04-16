class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        def bringToFirst(list, index):
            while index > 0: 
                list[index - 1], list[index] = list[index], list[index - 1]
                index -= 1

        p = [i for i in range(1, m + 1)]
        res = []
        for i in range(0, len(queries)):
            num = queries[i]
            index = p.index(num)
            res.append(index)
            bringToFirst(p, index)
        return res