class Solution(object):
    def intersection(self, nums):
        res = []

        if len(nums) == 1:
            return sorted(nums[0])

        for i in range(len(nums[0])):
            check = 1
            for j in range(1, len(nums)):
                if nums[0][i] in nums[j]:
                    check += 1
                if check == len(nums):
                    res.append(nums[0][i])
                    check = 1
                    break
        
        return sorted(res)