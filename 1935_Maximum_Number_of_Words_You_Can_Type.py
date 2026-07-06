class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        arr_text = text.split(" ")
        count = 0

        if len(brokenLetters) == 0:
            return len(arr_text)
        
        for i in range(len(arr_text)):
            for j in range(len(brokenLetters)):
                if brokenLetters[j] in arr_text[i]:
                    break
                if j == len(brokenLetters) - 1 and brokenLetters[j] not in arr_text[i]:
                    count += 1
        
        return count