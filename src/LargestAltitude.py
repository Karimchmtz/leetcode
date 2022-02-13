class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0]
        for g in gain:
            tmp = altitudes[len(altitudes) - 1]
            altitudes.append(tmp + g)
        return max(altitudes)