class Solution(object):
    def reverseVowels(self, s):
        arr = list(map(str, s))
        l = 0
        r = len(arr) - 1
        vowels = ['a', 'i', 'u', 'e', 'o']

        while l < r:
            if arr[l].lower() in vowels and arr[r].lower() in vowels:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            elif arr[l].lower() in vowels and arr[r].lower() not in vowels:
                r -= 1
            elif arr[l].lower() not in vowels and arr[r].lower() in vowels:
                l += 1
            elif arr[l].lower() not in vowels and arr[r].lower() not in vowels:
                l += 1
                r -= 1
        
        return ''.join(arr)