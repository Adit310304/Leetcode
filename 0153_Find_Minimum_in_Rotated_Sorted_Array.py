class Solution(object):
    def findMin(self, nums):
        count = nums[0]

        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                count = nums[i+1]
        return count