class Solution(object):
    def checkDivisibility(self, n):
        add = 0
        product = 1

        for i in range(len(str(n))):
            add += int(str(n)[i])
            product *= int(str(n)[i])
        
        if n % (add + product) == 0:
            return True
        
        return False