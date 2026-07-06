class Solution(object):
    def sortSentence(self, s):
        split_s = s.split(" ")
        arr = []

        for i in range(1, len(split_s) + 1):
            for j in range(len(split_s)):
                if int(split_s[j][-1]) == i:
                    arr.append(split_s[j][:len(split_s[j]) - 1])
                    break
        
        return ' '.join(arr)