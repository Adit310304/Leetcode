class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        res = 0

        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) > d:
                    count += 1
                if count == len(arr2):
                    res += 1
        
        return res