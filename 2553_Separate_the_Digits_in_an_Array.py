class Solution(object):
    def separateDigits(self, nums):
        res = []
        
        for i in range(len(nums)):
            mapping_str = list(map(str, str(nums[i])))
            res.extend(list(map(int, mapping_str)))
        
        return res