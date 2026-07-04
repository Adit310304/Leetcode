class Solution(object):
    def repeatedNTimes(self, nums):
        
        for i in range(len(nums)):
            count = nums.count(nums[i])
            if count * 2 == len(nums):
                return nums[i]