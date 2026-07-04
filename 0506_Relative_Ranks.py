class Solution(object):
    def findRelativeRanks(self, score):
        sorted_ranks = sorted(score, reverse=True)
        ranks = []

        for i in range(len(sorted_ranks)):
            if i == 0:
                ranks.append("Gold Medal")
            elif i == 1:
                ranks.append("Silver Medal")
            elif i == 2:
                ranks.append("Bronze Medal")
            else:
                ranks.append(str(i + 1))
        
        for i in range(len(score)):
            for j in range(len(sorted_ranks)):
                if sorted_ranks[j] == score[i]:
                    score[i] = ranks[j]
                    break
        
        return score