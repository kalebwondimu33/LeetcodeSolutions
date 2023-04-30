class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        mx=0
        for i in s:
            if i=="(":
                count+=1
                mx=max(count,mx)
            elif i==")":
                count-=1
        return mx
       
            
        