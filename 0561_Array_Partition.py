class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        result = 0

        for i in range(0, len(nums), 2):
            if nums[i] < nums[i+1]:
                result += nums[i]
            elif nums[i+1] < nums[i]:
                result += nums[i+1]
            elif nums[i] == nums[i+1]:
                result += nums[i]
        
        return result