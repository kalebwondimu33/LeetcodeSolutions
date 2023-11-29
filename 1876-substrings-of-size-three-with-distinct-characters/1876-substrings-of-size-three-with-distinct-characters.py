class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left=0
        right=2
        count=0
        while left<right and right<len(s):
            if len(s[left:right+1])==len(set(s[left:right+1])):
                count+=1
            left+=1
            right+=1
        return count
    
                    
        