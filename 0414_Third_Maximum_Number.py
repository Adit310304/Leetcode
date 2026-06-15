class Solution(object):
    def thirdMax(self, nums):
        sorted_nums = sorted(nums)
        count = 1

        for i in range(len(sorted_nums) - 2, -1, -1):
            if sorted_nums[i] != sorted_nums[i + 1]:
                count += 1
            if count == 3:
                return sorted_nums[i]
        
        return max(nums)