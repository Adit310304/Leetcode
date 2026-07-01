class Solution(object):
    def leftRightDifference(self, nums):
        left = []
        right = []
        
        for l in range(len(nums)):
            if l == 0:
                left.append(0)
            else:
                left.append(sum(nums[:l]))
        
        for r in range(len(nums)):
            if r == len(nums) - 1:
                right.append(0)
            else:
                right.append(sum(nums[r+1:]))
        
        for i in range(len(right)):
            left[i] = abs(left[i] - right[i])
        
        return left