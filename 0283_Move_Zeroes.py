class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        r = l + 1

        while l < len(nums) - 1:
            if r == len(nums) and l < r:
                l += 1
                r = l + 1
                continue
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
            
        return nums