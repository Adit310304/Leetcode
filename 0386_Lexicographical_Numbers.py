class Solution(object):
    def lexicalOrder(self, n):
        arr = [i for i in range(1, n + 1)]
        mapping = list(map(str, arr))
        return list(map(int, sorted(mapping)))