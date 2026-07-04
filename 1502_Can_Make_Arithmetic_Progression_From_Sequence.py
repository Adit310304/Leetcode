class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        sorted_arr = sorted(arr)
        distance = abs(sorted_arr[0] - sorted_arr[1])

        for i in range(len(arr) - 1):
            if abs(sorted_arr[i] - sorted_arr[i + 1]) != distance:
                return False
        
        return True