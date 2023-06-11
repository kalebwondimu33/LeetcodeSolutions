class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        left=0
        right=0
        count=0
        ransomNote=sorted(ransomNote)
        magazine=sorted(magazine)
        while left<len(ransomNote) and right<len(magazine):
            if ransomNote[left]==magazine[right]:
                left+=1
                right+=1
                count+=1
            else:
                right+=1
        if count==len(ransomNote):
            return True
        else:
            return False
        
            
        