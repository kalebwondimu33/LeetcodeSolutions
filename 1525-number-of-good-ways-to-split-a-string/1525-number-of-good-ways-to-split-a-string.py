class Solution:
    def numSplits(self, s: str) -> int:
        count=0
        left=[0]*len(s)
        unique=set()
        for i in range(len(s)):
            unique.add(s[i])
            left[i]=len(unique)
        unique.clear()
        for j in range(len(s)-1,0,-1):
            unique.add(s[j])
            if len(unique)==left[j-1]:
                count+=1
        return count
    
            
            
        