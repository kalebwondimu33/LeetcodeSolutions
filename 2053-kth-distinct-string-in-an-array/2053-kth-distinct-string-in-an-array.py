class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashtable={}
        for i in arr:
            if i not in hashtable:
                hashtable[i]=1
            else:
                hashtable[i]+=1
        truck=1
        for i in arr:
            if hashtable[i]==1:
                if truck==k:
                    return i
                truck+=1
        return ""
                
        
                
        