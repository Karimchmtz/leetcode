class Solution:
    def freqAlphabets(self, s: str) -> str:
    
        res = ""

        def parse(s: str) -> list[int]:
            i = len(s) - 1
            res = []
            buffer = ""
            while i >= 0:
                c = s[i]
                if c == "#":
                    c2 = s[i - 1]
                    c1 = s[i - 2]
                    buffer += c1
                    buffer += c2
                    i -= 3
                    res.append(int(buffer))
                    buffer = ""
                else:
                    res.append(int(c))
                    i -= 1
            res.reverse()
            return res

        l = parse(s)

        for elm in l:
            base = ord('a') - 1
            res += chr(base + elm)

        return res