class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count=0
        for i in range(26):
            l,r=s.find(chr(i+97)),s.rfind(chr(i+97))
            if l!=-1 and r!=-1:
                count+=len(set(s[l+1:r]))
        return count
    #time complexity o(n) and space complexity o(1)
            
                
        