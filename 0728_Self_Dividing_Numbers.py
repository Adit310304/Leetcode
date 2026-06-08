class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []

        for i in range(left, right + 1):
            str_number = str(i)
            true = 0
            for j in range(len(str_number)):
                if str_number[j] == "0":
                    continue
                if i % int(str_number[j]) == 0:
                    true += 1
                    if true == len(str_number):
                        res.append(i)
        
        return res