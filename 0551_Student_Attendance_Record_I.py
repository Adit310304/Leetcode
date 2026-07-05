class Solution(object):
    def checkRecord(self, s):
        countAbsences = s.count("A")
        countLate = 0

        for i in range(len(s)):
            if s[i] != "L":
                countLate = 0
            else:
                countLate += 1
            if countLate == 3 or countAbsences >= 2:
                return False
        
        return True
        