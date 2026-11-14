class Solution(object):
    def rearrangeArray(self, nums):
        set_nums = set(nums)
        list_set_nums = sorted(list(set_nums))
        ans = []
        
        while len(ans) < len(nums):
            for i in range(len(list_set_nums)):
                count_i_nums = nums.count(list_set_nums[i])
                count_i_ans = ans.count(list_set_nums[i])
                if count_i_ans < count_i_nums:
                    ans.append(list_set_nums[i])
        
        return ans