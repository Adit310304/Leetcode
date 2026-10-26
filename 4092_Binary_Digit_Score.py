class Solution(object):
    def calculateScore(self, a, b):
        bin_a = bin(a)[2:]
        bin_b = bin(b)[2:]

        sum_one_a = bin_a.count('1')
        sum_one_b = bin_b.count('1')

        if sum_one_a >= sum_one_b:
            return sum_one_a * sum_one_b
        else:
            return sum_one_b / sum_one_a