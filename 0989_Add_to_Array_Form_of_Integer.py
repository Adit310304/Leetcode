class Solution(object):
    def addToArrayForm(self, num, k):
        result = int(''.join(list(map(str, num)))) + k

        return list(map(int, str(result)))