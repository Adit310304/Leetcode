class Solution(object):
    def isPowerOfTwo(self, n):

        for i in range(100):
            if 2**i == n:
                return True
        
        return False