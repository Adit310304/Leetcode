class Solution(object):
    def minMoves(self, nums):
        count = 0

        for i in nums:
            count += abs(max(nums) - i)
        
        return count