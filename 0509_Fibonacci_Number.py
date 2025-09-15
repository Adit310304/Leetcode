class Solution(object):
    def fib(self, n):
        num1 = 0
        num2 = 1
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        for i in range(n-1):
            res = num1 + num2
            num1 = num2
            num2 = res
        
        return num2
        