class Solution(object):
    def reorderedPowerOf2(self, n):
        ans = sorted(str(n))

        for i in range(100):
            a = str(2**i)
            b = sorted(a)
            if b == ans:
                return True
        
        return False