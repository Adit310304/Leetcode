class Solution(object):
    def capitalizeTitle(self, title):
        lower = title.lower().split(" ")
        res = []

        for i in range(len(lower)):
            if len(lower[i]) > 2:
                res.append(lower[i].capitalize())
            else:
                res.append(lower[i])
        
        return ' '.join(res)