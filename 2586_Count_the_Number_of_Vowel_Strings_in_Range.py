class Solution(object):
    def vowelStrings(self, words, left, right):
        count = 0
        vowels = ["a", "i", "u", "e", "o"]

        for i in range(left, right + 1):
            if len(words[i]) == 1 and words[i] in vowels:
                count += 1
            elif len(words[i]) > 1:
                if words[i][0] in vowels and words[i][-1] in vowels:
                    count += 1
        
        return count