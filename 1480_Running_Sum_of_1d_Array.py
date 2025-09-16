class Solution(object):
    def runningSum(self, nums):
        k = nums[0]

        for i in range(1, len(nums)):
            k += nums[i]
            nums[i] = k

        return nums