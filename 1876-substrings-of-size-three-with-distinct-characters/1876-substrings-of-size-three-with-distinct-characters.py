class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left=0
        mid=1
        right=2
        count=0
        while left<mid<right<len(s):
            if s[left]!=s[mid] and s[mid]!=s[right] and s[left]!=s[right]:
                count+=1
                left+=1
                right+=1
                mid+=1
            else:
                left+=1
                right+=1
                mid+=1
        return count
                    
        