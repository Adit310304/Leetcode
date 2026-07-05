class Solution(object):
    def findTheDifference(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        index = 0
        res = ''
        
        if len(s) == 0:
            return t
        
        while len(sorted_s) > 0:
            if sorted_s[index] == sorted_t[index]:
                sorted_s.pop(index)
                sorted_t.pop(index)
            elif sorted_s[index] != sorted_t[index]:
                res += sorted_t[index]
                sorted_t.pop(index)
            if len(sorted_s) == 0:
                res += ''.join(sorted_t[:])
        
        return res