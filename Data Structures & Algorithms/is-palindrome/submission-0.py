class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''
        for char in s:
            if char.isalnum():
                alnum += char.lower()
        return alnum==alnum[::-1]
        