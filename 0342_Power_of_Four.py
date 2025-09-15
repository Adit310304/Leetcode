class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(100):
            if 4**i == n:
                return True
        
        return False