class Solution(object):
    def countSpecialIntegers(self, nums):
        res = 0
        arr_unique = list(set(nums))
        
        for i in range(len(arr_unique)):
            check = []
            if nums.count(arr_unique[i]) == 3:
                for j in range(len(nums)):
                    if nums[j] == arr_unique[i]:
                        check.append(j)
                if check[1] - check[0] == check[2] - check[1]:
                    res += 1
        
        return res