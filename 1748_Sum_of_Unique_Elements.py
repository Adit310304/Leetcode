class Solution(object):
    def sumOfUnique(self, nums):
        arr = [0]*(max(nums)+1)
        res = 0

        for i in range(len(nums)):
            arr[nums[i]] += 1

        for j in range(len(arr)):
            if arr[j] == 1:
                res += j
        
        return res