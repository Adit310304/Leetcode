class Solution(object):
    def digitFrequencyScore(self, n):
        mapping = list(map(int, str(n)))
        sets = set(list(map(int, str(n))))
        res = 0
        
        for i in sets:
            count = mapping.count(i) * i
            res += count
        
        return res