class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2

        merged.sort()

        if (len(merged)) % 2 != 0:
            return merged[((len(merged))//2)]
        
        if (len(merged)) % 2 == 0:
            mid1 = merged[(len(merged)//2)-1]
            mid2 = merged[(len(merged))//2]
            return (mid1 + mid2) / 2.0
        