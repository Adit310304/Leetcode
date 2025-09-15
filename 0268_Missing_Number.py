class Solution(object):
    def missingNumber(self, nums):
        max_val = 0

        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]

        for j in range(0, max_val + 2):
            if j not in nums:
                return j
        
        return 0