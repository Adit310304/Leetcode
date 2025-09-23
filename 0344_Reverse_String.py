class Solution(object):
    def reverseString(self, s):
        l = 0
        r = -1

        for i in range(len(s)//2):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1