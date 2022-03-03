class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        res = 0
        for i in range(0, len(startTime)):
            start = startTime[i]
            end = endTime[i]
            qTime = queryTime
            if (qTime <= end and qTime >= start):
                res += 1
        return res