class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_index = 0
        count = 0
        sort_ransomNote = sorted(ransomNote)
        sort_magazine = sorted(magazine)

        for i in range(len(sort_magazine)):
            if ransom_index == len(sort_ransomNote):
                break
            if sort_ransomNote[ransom_index] == sort_magazine[i]:
                count += 1
                ransom_index += 1

        if count == len(sort_ransomNote):
            return True
        else:
            return False