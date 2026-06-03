class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ''

        index = 0

        while True:
            if index == len(word1):
                res += word2[index:]
                break
            elif index == len(word2):
                res += word1[index:]
                break
            res += word1[index]
            res += word2[index]
            index += 1

        return res