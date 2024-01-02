class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase=""
        for i in s:
            if i.isalnum():
                phrase+=i.lower()
        if phrase==phrase[::-1]:
            return True
        else:
            return False
        