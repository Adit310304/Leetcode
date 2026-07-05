class Solution(object):
    def finalValueAfterOperations(self, operations):
        start = 0

        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                start -= 1
            else:
                start += 1
        
        return start