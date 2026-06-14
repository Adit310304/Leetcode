class Solution(object):
    def detectCapitalUse(self, word):
        if word == word.upper() or word == word.lower() or word == word.capitalize():
            return True
        else:
            return False