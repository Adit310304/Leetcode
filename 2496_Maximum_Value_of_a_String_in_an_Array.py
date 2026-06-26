class Solution(object):
    def maximumValue(self, strs):
        maximum = 0

        for i in range(len(strs)):
            if strs[i].isdigit():
                if int(strs[i]) > maximum:
                    maximum = int(strs[i])
            elif strs[i].isalnum():
                if len(strs[i]) > maximum:
                    maximum = len(strs[i])
        
        return maximum