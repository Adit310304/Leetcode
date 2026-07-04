class Solution(object):
    def countCharacters(self, words, chars):
        res = 0

        for i in range(len(words)):
            check = 0
            for j in range(len(words[i])):
                count_words = words[i].count(words[i][j])
                count_chars = chars.count(words[i][j])
                if count_chars >= count_words:
                    check += 1
                if check == len(words[i]):
                    res += len(words[i])

        return res