class Solution(object):
    def consecutiveSetBits(self, n):
        binary = int(bin(n)[2:])
        str_binary = str(binary)
        count = 0
        
        for i in range(len(str_binary) - 1):
            if str_binary[i] == "1" and str_binary[i + 1] == "1":
                count += 1

        if count == 1:
            return True
        else:
            return False