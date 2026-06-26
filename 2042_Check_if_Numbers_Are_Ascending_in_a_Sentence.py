class Solution(object):
    def areNumbersAscending(self, s):
        arr = s.split(" ")
        check = 0

        for i in range(len(arr)):
            if arr[i].isdigit():
                if int(arr[i]) > check:
                    check = int(arr[i])
                else:
                    return False
            
        return True