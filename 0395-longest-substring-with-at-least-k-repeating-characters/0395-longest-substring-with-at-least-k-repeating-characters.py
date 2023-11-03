class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        st=0
        c=Counter(s)
        for i,v in enumerate(s):
            if c[v]<k:
                return max(self.longestSubstring(s[st:i],k),self.longestSubstring(s[i+1:],k))
        return len(s)
                
        
        