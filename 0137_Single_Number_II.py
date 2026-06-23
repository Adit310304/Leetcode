from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        dictionary = Counter(nums)

        for k, v in dictionary.items():
            if v == 1:
                return k