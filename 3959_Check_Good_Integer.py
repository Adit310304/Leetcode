class Solution(object):
    def checkGoodInteger(self, n):
        str_n = str(n)
        digitSum = 0
        squareSum = 0

        for i in range(len(str_n)):
            digitSum += int(str_n[i])
            squareSum += int(str_n[i]) ** 2
        
        return True if squareSum - digitSum >= 50 else False