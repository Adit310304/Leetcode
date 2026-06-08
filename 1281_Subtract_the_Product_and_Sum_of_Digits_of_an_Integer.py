class Solution(object):
    def subtractProductAndSum(self, n):
        str_n = str(n)
        productDigits = 1
        sumDigits = 0

        for i in range(len(str_n)):
            productDigits *= int(str_n[i])
            sumDigits += int(str_n[i])
        
        return productDigits - sumDigits