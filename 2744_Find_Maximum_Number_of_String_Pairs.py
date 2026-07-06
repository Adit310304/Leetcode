class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        arr = []

        for i in range(len(words)):
            arr.append(''.join(sorted(words[i])))
        
        sett = set(arr)
        count = 0

        for i in sett:
            check = arr.count(i)
            if check == 2:
                count += 1
        
        return count