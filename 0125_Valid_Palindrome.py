class Solution(object):
    def isPalindrome(self, s):
        whitespace = s.replace(' ', '')
        sentence = ''

        for i in range(len(whitespace)):
            if whitespace[i].isalnum():
                sentence += whitespace[i]
        
        return True if sentence.lower() == sentence[::-1].lower() else False