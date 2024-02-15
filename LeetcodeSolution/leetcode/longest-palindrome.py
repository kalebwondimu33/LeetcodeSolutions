class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = sum([(x//2) * 2 for x in Counter(s).values()])
        return count if count == len(s) else (count + 1)
                
        