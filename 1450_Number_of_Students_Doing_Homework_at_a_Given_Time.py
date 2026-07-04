class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        res = 0

        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                res += 1
        
        return res