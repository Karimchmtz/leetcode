class Solution(object):
    def euclideanDistance(self, coordinate1, coordinate2):
        return pow(pow(coordinate1[0] - coordinate2[0], 2) + pow(coordinate1[1]     - coordinate2[1], 2), .5)

    def countPoints(self, points, queries):
        res = []
        for j in queries:
            count = 0
            for p in points:
                distance = Solution.euclideanDistance(self, p, j)
                if (distance <= j[2]):
                    count += 1
            res.append(count)
        return res