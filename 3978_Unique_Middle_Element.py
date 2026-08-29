class Solution(object):
    def isMiddleElementUnique(self, nums):
        num = nums[len(nums) // 2]

        if nums.count(num) > 1:
            return False
        else:
            return True