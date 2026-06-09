class Solution(object):
    def convertDateToBinary(self, date):
        split = date.split("-")
        binary = []

        for i in range(len(split)):
            split[i] = int(split[i])
            binary.append(str(int(bin(split[i])[2:])))
        
        return "-".join(binary)