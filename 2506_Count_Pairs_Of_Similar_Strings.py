class Solution(object):
    def similarPairs(self, words):
        count = 0

        for i in range(len(words) - 1):
            set_i = set(words[i])
            for j in range(i + 1, len(words)):
                set_j = set(words[j])
                if set_i == set_j:
                    count += 1
        
        return count
