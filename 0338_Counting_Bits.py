class Solution(object):
    def countBits(self, n):
        res = []

        for i in range(n + 1):
            bit = int(bin(i)[2:])
            int_arr = list(map(int, str(bit)))
            res.append(sum(int_arr))
        
        return res