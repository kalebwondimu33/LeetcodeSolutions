class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #add 0 to the first house 
        prefix=[0]
        cur=0
        for i in travel:
            cur+=i
            prefix.append(cur)
        M_idx=P_idx=G_idx=0
        res=0
        for i in range(len(garbage)):
            res+=len(garbage[i])
            if "M" in garbage[i]:
                M_idx=i
            if "G" in garbage[i]:
                G_idx=i
            if "P" in garbage[i]:
                P_idx=i
        res+=prefix[M_idx]
        res+=prefix[G_idx]
        res+=prefix[P_idx]
        return res
        
        
            
                
                
            