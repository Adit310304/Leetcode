class Solution(object):
    def findClosestNumber(self, nums):
        minimum = max(nums)

        for i in range(len(nums)):
            if abs(nums[i]) < abs(minimum):
                minimum = nums[i]
        
        if minimum < 0 and -(minimum) in nums:
            return -(minimum)
        else:
            return minimum