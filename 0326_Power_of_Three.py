class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(100):
            if 3**i == n:
                return True

        return False