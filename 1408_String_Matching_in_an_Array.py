class Solution(object):
    def stringMatching(self, words):
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    pass
                elif words[i] in words[j] and words[i] not in res:
                    res.append(words[i])
                elif words[j] in words[i] and words[j] not in res:
                    res.append(words[j])
            
        return res