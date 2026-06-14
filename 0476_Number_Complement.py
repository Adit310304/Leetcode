class Solution(object):
    def findComplement(self, num):
        bit = str(int(bin(num)[2:]))
        res = 0

        for i in range(1, len(bit) + 1):
            if bit[-i] == "1":
                continue
            else:
                res += 2 ** (i - 1)
        
        return res