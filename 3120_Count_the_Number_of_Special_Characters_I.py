class Solution(object):
    def numberOfSpecialChars(self, word):
        sett = set(word.lower())
        count = 0
        
        for i in sett:
            if i.lower() in word and i.upper() in word:
                count += 1
        
        return count