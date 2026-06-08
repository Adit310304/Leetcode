class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > max:
                    max = count
            else:
                count = 0
        
        return max