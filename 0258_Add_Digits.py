class Solution(object):
    def addDigits(self, num):
        result = num
        sum = 0

        for i in range(len(str(num))):
            if len(str(result)) == 1:
                break
            for j in str(result):
                sum += int(j)
            result = sum
            sum = 0

        return result