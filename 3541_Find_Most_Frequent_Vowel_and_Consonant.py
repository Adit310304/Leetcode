class Solution(object):
    def maxFreqSum(self, s):
        arr = list(map(str, s))
        v = 0
        c = 0

        vowel = ["a", "i", "u", "e", "o"]

        for i in range(len(s)):
            if s[i] in vowel:
                count_v = arr.count(s[i])
                if count_v > v:
                    v = count_v
            elif s[i] not in vowel:
                count_c = arr.count(s[i])
                if count_c > c:
                    c = count_c
        
        return v + c