class Solution(object):
    def minMergedInteger(self, nums):
        arr = []

        for i in range(0, len(nums) - 1, 2):
            arr.append(str(nums[i]) + str(nums[i + 1]))
        
        mapping = list(map(int, arr))
        return min(mapping)