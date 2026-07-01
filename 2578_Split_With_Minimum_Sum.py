class Solution(object):
    def splitNum(self, num):
        sorted_a = sorted(str(num))
        even = ''
        odd = ''

        for i in range(len(sorted_a)):
            if i == 0 or i % 2 == 0:
                even += sorted_a[i]
            else:
                odd += sorted_a[i]
        
        return int(even) + int(odd)