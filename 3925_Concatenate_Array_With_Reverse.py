class Solution(object):
    def concatWithReverse(self, nums):
        
        for i in range(len(nums) - 1, -1, -1):
            nums.append(nums[i])
        
        return nums