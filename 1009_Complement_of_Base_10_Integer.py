class Solution(object):
    def bitwiseComplement(self, n):
        binary = int(bin(n)[2:])
        str_binary = str(binary)
        len_str_binary = len(str_binary) - 1
        res = 0

        for i in range(len(str_binary)):
            if str_binary[i] == "1":
                res += 0 * (2 ** len_str_binary)
                len_str_binary -= 1
            else:
                res += 1 * (2 ** len_str_binary)
                len_str_binary -= 1
        
        return res