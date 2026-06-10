class Solution(object):
    def repeatedCharacter(self, s):
        check = []

        for i in range(len(s)):
            if s[i] not in check:
                check.append(s[i])
            else:
                return s[i]