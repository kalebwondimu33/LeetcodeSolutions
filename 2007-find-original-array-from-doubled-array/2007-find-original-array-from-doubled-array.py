class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c=Counter(changed)
        if c[0]%2:
            return []
        for x in sorted(c):
            if c[x]>c[2*x]:
                return []
            c[2*x]-=c[x] if x else c[x]//2
        return list(c.elements())
    
        
    
                
        