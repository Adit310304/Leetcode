class Solution(object):
    def sumOfMultiples(self, n):
        result = 0

        for i in range(3, n+1):
            if i%3 == 0:
                result += i
                continue
            if i%5 == 0:
                result += i
                continue
            if i%7 == 0:
                result += i
                continue
        return result