class Solution(object):
    def uniqueOccurrences(self, arr):
        sett = set(arr)
        check = []

        for i in sett:
            count = arr.count(i)
            if count in check:
                return False
            else:
                check.append(count)
                
        return True