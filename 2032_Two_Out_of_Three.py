class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        nums4 = nums1 + nums2 + nums3
        sort = set(nums4)

        arr = []
        arr.append(nums1)
        arr.append(nums2)
        arr.append(nums3)

        res = []
        count = 0
        
        for i in sort:
            for j in range(len(arr)):
                if i in arr[j]:
                    count += 1
            if count >= 2:
                res.append(i)
            count = 0
        
        return res