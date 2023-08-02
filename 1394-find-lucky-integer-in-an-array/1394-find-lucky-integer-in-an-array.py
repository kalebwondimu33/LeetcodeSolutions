class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashtable={}
        result=[]
        for i in arr:
            if i in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1
        for i in hashtable:
            if i==hashtable[i]:
                result.append(i)
        if not result:
            return -1
        return max(result)
        