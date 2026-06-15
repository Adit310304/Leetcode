class Solution(object):
    def findDuplicate(self, nums):

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return sorted_nums[i]