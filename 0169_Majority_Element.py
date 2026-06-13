class Solution(object):
    def majorityElement(self, nums):
        sorted_nums = sorted(nums)
        count = 1
        curr = sorted_nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == curr:
                count += 1
            if sorted_nums[i] != curr:
                curr = sorted_nums[i]
            if count > int(len(nums) / 2):
                return curr