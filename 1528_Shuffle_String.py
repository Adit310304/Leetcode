class Solution(object):
    def restoreString(self, s, indices):
        arr = [0] * len(indices)

        for i in range(len(indices)):
            arr[indices[i]] = s[i]

        return ''.join(arr)