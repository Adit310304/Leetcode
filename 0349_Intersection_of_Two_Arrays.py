class Solution(object):
    def intersection(self, nums1, nums2):
        res = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] not in res:
                    res.append(nums1[i])

        return res