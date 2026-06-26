class Solution(object):
    def vowelConsonantScore(self, s):
        v = 0
        c = 0

        vowel = ["a", "i", "u", "e", "o"]

        for i in range(len(s)):
            if s[i] in vowel:
                v += 1
            elif s[i] not in vowel and s[i].isalpha():
                c += 1

        return int(v/c) if c != 0 else 0