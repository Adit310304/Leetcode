class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        str_firstWord = ''
        str_secondWord = ''
        str_targetWord = ''
        
        for i in range(len(firstWord)):
            str_firstWord += str(ord(firstWord[i]) - ord('a'))
            
        for j in range(len(secondWord)):
            str_secondWord += str(ord(secondWord[j]) - ord('a'))
        
        for k in range(len(targetWord)):
            str_targetWord += str(ord(targetWord[k]) - ord('a'))
        
        return int(str_firstWord) + int(str_secondWord) == int(str_targetWord)