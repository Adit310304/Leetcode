class Solution(object):
    def digitCount(self, num):
        
        for i in range(len(num)):
            count = num.count(str(i))
            if count != int(num[i]):
                return False
        
        return True