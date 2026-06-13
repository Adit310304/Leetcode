class Solution(object):
    def reverseWords(self, s):
        split_s = s.strip().split(" ")
        res = ''

        for i in range(len(split_s) - 1, -1, -1):
            if split_s[i] == '':
                continue
            if i == 0:
                res += split_s[i]
                break
            res += split_s[i] + ' '
        
        return res