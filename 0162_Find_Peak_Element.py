class Solution(object):
    def findPeakElement(self, nums):
        max_val = nums[0]

        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
        
        for j in range(len(nums)):
            if nums[j] == max_val:
                return j