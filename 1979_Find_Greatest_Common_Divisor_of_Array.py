class Solution(object):
    def findGCD(self, nums):
        res = 0

        for i in range(1, min(nums) + 1):
            if min(nums) % i == 0 and max(nums) % i == 0:
                res = i
        
        return res