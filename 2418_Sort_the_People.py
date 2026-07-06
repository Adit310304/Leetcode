class Solution(object):
    def sortPeople(self, names, heights):
        zipping = list(zip(names, heights))
        sorted_zipping = sorted(zipping, key=lambda zipper: zipper[1], reverse=True)

        res = []

        for i in range(len(sorted_zipping)):
            res.append(sorted_zipping[i][0])
        
        return res