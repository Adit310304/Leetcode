from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        dictionary = Counter(arr)
        lucky = 0

        for k, v in dictionary.items():
            if k == v:
                lucky = v
        
        if lucky != 0:
            return lucky
        else:
            return -1