class Solution(object):
    def reverseWords(self, s):
        res = ''
        split_s = s.split(" ")

        for i in range(len(split_s)):
            if i == len(split_s) - 1:
                res += split_s[i][::-1]
                break
            res += split_s[i][::-1] + " "
        
        return res
        