class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left=1
        lf=0
        while left<=len(haystack):
            if haystack[lf:left]==needle:
                return lf
            elif len(haystack[lf:left])<len(needle) and haystack[lf:left]!=needle:
                left+=1
            else:
                lf+=1
                left+=1
        return -1
            
                
            
        