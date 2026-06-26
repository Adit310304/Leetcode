class Solution(object):
    def findTheArrayConcVal(self, nums):
        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            str_int = ''
            str_int += str(nums[left]) + str(nums[right])
            count += int(str_int)
            left += 1
            right -= 1
        
        if len(nums) % 2 != 0:
            count += nums[int(len(nums) / 2)]
        
        return count