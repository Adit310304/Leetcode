class Solution(object):
    def countSegments(self, s):
        count = 0
        arr = s.strip().split(" ")

        for i in range(len(arr)):
            if arr[i] != "":
                count += 1
        
        return count