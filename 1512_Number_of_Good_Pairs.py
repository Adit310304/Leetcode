class Solution(object):
    def numIdenticalPairs(self, nums):
        sett = set(nums)
        res = 0

        for i in sett:
            count = nums.count(i)
            calc = (count * (count - 1)) // 2
            res += calc
        
        return res