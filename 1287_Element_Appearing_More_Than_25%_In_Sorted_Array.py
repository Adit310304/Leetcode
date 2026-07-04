class Solution(object):
    def findSpecialInteger(self, arr):
        appear = (25 * len(arr)) / 100
        
        for i in range(len(arr)):
            count = arr.count(arr[i])
            if count > int(appear):
                return arr[i]