class Solution(object):
    def romanToInt(self, s):
        integer = [1, 5, 10, 50, 100, 500, 1000]
        symbol = ["I", "V", "X", "L", "C", "D", "M"]

        res = 0
        curr = 0

        for i in range(len(s)):
            for j in range(len(symbol)):
                if s[i] == symbol[j]:
                    if i == 0:
                        res += integer[j]
                        curr = integer[j]
                    else:
                        if curr < integer[j]:
                            res -= curr * 2
                            res += integer[j]
                            curr = integer[j]
                        else:
                            res += integer[j]
                            curr = integer[j]
        
        return res