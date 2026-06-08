class Solution(object):
    def findMaxK(self, nums):
        max = 0

        for i in range(len(nums)):
            if (nums[i] * (-1)) in nums:
                if abs(nums[i]) > max:
                    max = abs(nums[i])
        
        if max == 0:
            return -1
        else:
            return max