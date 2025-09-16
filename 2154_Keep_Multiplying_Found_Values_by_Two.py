class Solution(object):
    def findFinalValue(self, nums, original):
        res = original

        if original not in nums:
            return original

        while res in nums:
            count = res*2
            res = count
        
        return res
        