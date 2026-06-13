class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        index_1 = 0
        index_2 = 0

        while True:
            if index_1 == len(nums1) or index_2 == len(nums2):
                break
            if sorted_nums1[index_1] < sorted_nums2[index_2]:
                index_1 += 1
                continue
            elif sorted_nums2[index_2] < sorted_nums1[index_1]:
                index_2 += 1
                continue
            if sorted_nums1[index_1] == sorted_nums2[index_2]:
                res.append(sorted_nums1[index_1])
                index_1 += 1
                index_2 += 1
        
        return res