class Solution(object):
    def pivotInteger(self, n):
        arr = [i for i in range(1, n + 1)]

        if n == 1:
            return 1

        for i in range(1, len(arr)):
            if sum(arr[0:i]) == sum(arr[i-1:]):
                return i
        
        return -1