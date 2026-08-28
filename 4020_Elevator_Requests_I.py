class Solution(object):
    def elevatorRequests(self, n, requests):
        curr = 0
        res = 0

        for i in range(len(requests)):
            curr = abs(curr - requests[i])
            res += curr
            curr = requests[i]
        
        return res