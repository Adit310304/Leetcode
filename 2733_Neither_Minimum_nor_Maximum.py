class Solution(object):
    def findNonMinOrMax(self, nums):
        for i in range(len(nums)):
            if nums[i] != max(nums) and nums[i] != min(nums):
                return nums[i]
        
        return -1