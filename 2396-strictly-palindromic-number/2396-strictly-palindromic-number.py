class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def reverse(n,b):
            rev=0
            while n:
                rev+=rev*b+n%b
                n//=b
            return rev
        for b in range(2,n-1):
            rev=reverse(n,b)
            if n!=rev:
                return False
        return True
            
            
            
            
            