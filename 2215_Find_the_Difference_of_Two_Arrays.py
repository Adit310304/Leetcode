class Solution(object):
    def findDifference(self, nums1, nums2):
        res_nums1 = []
        res_nums2 = []

        for i in nums1:
            if i not in nums2 and i not in res_nums1:
                res_nums1.append(i)
        
        for j in nums2:
            if j not in nums1 and j not in res_nums2:
                res_nums2.append(j)
        
        return [res_nums1, res_nums2]