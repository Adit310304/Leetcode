class Solution(object):
    def greatestLetter(self, s):
        res = ''

        for i in "abcdefghijklmnopqrstuvwxyz":
            if i.upper() in s and i.lower() in s:
                res = i
        
        return res.upper()