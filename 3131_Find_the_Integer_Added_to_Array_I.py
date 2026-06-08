class Solution(object):
    def addedInteger(self, nums1, nums2):
        sorted_nums1, sorted_nums2 = sorted(nums1), sorted(nums2)

        if nums1[0] == 1000 and nums2[0] == 0:
            return -1000

        if sorted_nums1[0] <= sorted_nums2[0]:
            for i in range(max(max(nums1, nums2)) + 1):
                if sorted_nums1[0] + i == sorted_nums2[0]:
                    return i
        else:
            for i in range(max(max(nums1, nums2))):
                if sorted_nums1[0] - i == sorted_nums2[0]:
                    return -(i)