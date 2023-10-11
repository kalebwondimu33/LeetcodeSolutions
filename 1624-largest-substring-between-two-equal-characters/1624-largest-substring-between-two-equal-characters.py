class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        large=-1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    large=max(large,j-i-1)
        return large
                
        