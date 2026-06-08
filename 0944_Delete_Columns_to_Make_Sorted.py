class Solution(object):
    def minDeletionSize(self, strs):
        delete = 0
        check = ''

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                check += strs[j][i]
            if check != ''.join(sorted(check)):
                delete += 1
            check = ''

        return delete