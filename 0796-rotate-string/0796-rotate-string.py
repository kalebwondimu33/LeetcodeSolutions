class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i+1:]+s[:i+1]==goal:
                return True
        return False
        