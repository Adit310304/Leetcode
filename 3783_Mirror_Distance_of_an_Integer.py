class Solution(object):
    def mirrorDistance(self, n):
        reverse = str(n)[::-1]
        return abs(n - int(reverse))