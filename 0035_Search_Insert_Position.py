class Solution(object):
    def searchInsert(self, nums, target):
        left = 0

        while left < len(nums):
            if target < min(nums):
                return 0
            if nums[left] == target:
                return left
            if left == len(nums) - 1:
                return len(nums)
            else:
                if nums[left] < target and nums[left + 1] > target:
                    return left + 1
            left += 1