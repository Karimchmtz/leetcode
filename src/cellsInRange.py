class Solution:
    def cellsInRange(self, s: str):
        nbcols = ord(s[3]) - ord(s[0]) + 1
        nbrows = int(s[4]) - int(s[1]) + 1
        start_cols = s[0]
        start_rows = int(s[1])
        res = []
        for i in range(0, nbcols):
            for j in range(0, nbrows):
                buffer = ""
                buffer += chr(ord(start_cols) + i)
                buffer += str(start_rows + j)
                res.append(buffer)
        return res