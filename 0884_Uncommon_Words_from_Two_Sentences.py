class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        arr_s1 = s1.split(" ")
        arr_s2 = s2.split(" ")
        res = []

        for i in range(len(arr_s1)):
            count = arr_s1.count(arr_s1[i])
            if count < 2 and arr_s1[i] not in arr_s2:
                res.append(arr_s1[i])
        
        for j in range(len(arr_s2)):
            count = arr_s2.count(arr_s2[j])
            if count < 2 and arr_s2[j] not in arr_s1:
                res.append(arr_s2[j])
        
        return res