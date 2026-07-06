class Solution(object):
    def areOccurrencesEqual(self, s):
        sett = set(s)
        count = s.count(s[0])

        for i in sett:
            check = s.count(i)
            if check != count:
                return False
        
        return True