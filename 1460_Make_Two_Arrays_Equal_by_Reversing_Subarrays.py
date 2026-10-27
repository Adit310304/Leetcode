class Solution(object):
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()

        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        
        return True