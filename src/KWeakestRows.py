class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        res = []
        for i in range(0, len(mat)):
            soldiers = 0
            for j in mat[i]:
                if j == 1:
                    soldiers += 1
            res.append((i, soldiers))
        res.sort(key=lambda tup: tup[1])
        res2 = []
        for (a,b) in res:
            if (len(res2) == k):
                break
            res2.append(a)
        return res2