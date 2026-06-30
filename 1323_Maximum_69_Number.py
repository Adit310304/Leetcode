class Solution(object):
    def maximum69Number (self, num):
        maximum = num
    
        for i in range(len(str(num))):
            mapping = list(map(str, str(num)))
            if mapping[i] == '9':
                mapping[i] = '6'
            elif mapping[i] == '6':
                mapping[i] = '9'
            if int(''.join(mapping)) > maximum:
                maximum = int(''.join(mapping))
        
        return maximum