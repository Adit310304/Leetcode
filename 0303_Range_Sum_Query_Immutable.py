class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        

    def sumRange(self, left, right):
        count = 0

        for i in range(left, right + 1):
            count += self.nums[i]
        
        return count
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)