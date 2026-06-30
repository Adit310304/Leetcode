class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        
        for i in range(k):
            minimum = min(nums)
            for j in range(len(nums)):
                if nums[j] == minimum:
                    nums[j] *= multiplier
                    break
        
        return nums