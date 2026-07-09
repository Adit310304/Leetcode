class Solution(object):
    def sortArrayByParityII(self, nums):
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]
        res = []

        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        
        return res