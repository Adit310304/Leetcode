class Solution(object):
    def singleNonDuplicate(self, nums):
        res = 0

        for i in range(len(nums)):
            res ^= nums[i]

        return res