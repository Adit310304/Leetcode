class Solution(object):
    def removeAnagrams(self, words):
        index = 1
        curr = words[0]

        while index < len(words):
            if sorted(words[index]) == sorted(curr):
                words.pop(index)
            else:
                index += 1
                curr = words[index - 1]
        
        return words