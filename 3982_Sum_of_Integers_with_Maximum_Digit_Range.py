class Solution(object):
    def maxDigitRange(self, nums):
        check = []

        for i in range(len(nums)):
            mapping = list(map(int, str(nums[i])))
            count = max(mapping) - min(mapping)
            check.append(count)
        
        maximum = max(check)
        res = 0

        for j in range(len(check)):
            if check[j] == maximum:
                res += nums[j]
        
        return res