class Solution(object):
    def plusOne(self, digits):
        mapping = list(map(str, digits))
        str_digits = ''.join(mapping)
        add = int(str_digits) + 1
        
        return list(map(int, str(add)))