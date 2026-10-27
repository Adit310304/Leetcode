class Solution(object):
    def numberOfSteps(self, num):
        count = num
        res = 0

        while count > 0:
            if count % 2 == 0:
                count = count / 2
                res += 1
            else:
                count -= 1
                res += 1
        
        return res