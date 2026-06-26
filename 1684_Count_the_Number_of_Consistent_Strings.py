class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0

        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    break
                if j == len(words[i]) - 1:
                    count += 1
        
        return count