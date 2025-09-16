class Solution(object):
    def sortArrayByParity(self, nums):
        result = []

        for i in range(len(nums)):
            if nums[i]%2 == 0:
                result.append(nums[i])

        for j in range(len(nums)):
            if nums[j]%2 == 1:
                result.append(nums[j])


        return result    