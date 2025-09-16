class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        res_nums1 = [i for i in nums1 if i in nums2]
        res_nums2 = [j for j in nums2 if j in nums1]

        return [len(res_nums1), len(res_nums2)]