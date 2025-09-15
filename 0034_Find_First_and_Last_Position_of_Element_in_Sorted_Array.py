class Solution(object):
    def searchRange(self, nums, target):
        res = []

        if len(nums) == 1 and nums[0] == target:
            return [0,0]

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        if len(res) == 2:
                return res
        if len(res) == 1:
            return [res[0],res[0]]
        if len(res) > 2:
            return [res[0],res[-1]]
        
        return [-1,-1]