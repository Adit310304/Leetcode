class Solution(object):
    def isSubsequence(self, s, t):
        count = 0
        s_index = 0

        if s == '':
            return True

        for i in range(len(t)):
            if s_index == len(s):
                break
            if s[s_index] == t[i]:
                count += 1
                s_index += 1
        
        if count == len(s):
            return True
        else:
            return False