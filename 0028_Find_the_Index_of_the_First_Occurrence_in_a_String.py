class Solution(object):
    def strStr(self, haystack, needle):
        left = 0
        right = left + len(needle)

        if len(haystack) == len(needle):
            if haystack == needle:
                return 0
        elif len(haystack) != 1 and len(needle) == 1:
            for i in range(len(haystack)):
                if haystack[i] == needle:
                    return i

        while right < len(haystack) + 1:
            if list(map(str, haystack[left:right])) == list(map(str, needle)):
                return left
            else:
                left += 1
                right = left + len(needle)
        
        return -1