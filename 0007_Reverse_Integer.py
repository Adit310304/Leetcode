class Solution(object):
    def reverse(self, x):
        str_x = str(x)
        mapping = list(map(str, str(x)))

        if mapping[0].isdigit():
            if int(''.join(mapping[::-1])) > 2**31:
                return 0
            return int(''.join(mapping[::-1]))
        else:
            mapping.pop(0)
            if -(int(''.join(mapping[::-1]))) < -(2**31):
                return 0
            return -(int(''.join(mapping[::-1])))