class Solution(object):
    def lengthOfLastWord(self, s):
        fix_s = s.strip()
        arr_s = fix_s.split()
        return len(arr_s[-1])