class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashtable={}
        gre=0
        res=0
        for i in arr:
            if i in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1
        for i in hashtable:
            if hashtable[i]>gre:
                gre=hashtable[i]
                res=i
        return res
        
        