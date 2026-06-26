class Solution(object):
    def getLucky(self, s, k):
        str_int = ''

        for i in range(len(s)):
            str_int += str(ord(s[i]) - ord('a') + 1)
        
        res = 0

        for i in range(k):
            for j in range(len(str_int)):
                res += int(str_int[j])
            if i == k - 1:
                return res
            str_int = str(res)
            res = 0
        
        return res