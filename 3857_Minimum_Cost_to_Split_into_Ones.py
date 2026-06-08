class Solution(object):
    def minCost(self, n):
        cost = 0

        for i in range(n - 1, 0, -1):
            cost += i
        
        return cost