class Solution(object):
    def maxProduct(self, n):
        str_n = str(n)
        mapping = list(map(int, str_n))
        mapping.sort()

        if len(mapping) == 2:
            return int(mapping[0]) * int(mapping[1])

        return int(mapping[-1]) * int(mapping[-2])