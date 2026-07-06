class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0

        for i in range(len(sentences)):
            split = sentences[i].split(" ")
            if len(split) > count:
                count = len(split)
        
        return count