class Solution(object):
    def singleNumber(self, nums):
        res = []
        nums.sort()

        if len(nums) <= 2:
            return nums

        if nums[0] != nums[1]:
            res.append(nums[0])
        if nums[len(nums)-1] != nums[len(nums)-2]:
            res.append(nums[len(nums)-1])

        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                res.append(nums[i])

        return res