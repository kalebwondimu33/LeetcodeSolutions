class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        dic={}
        result=[]
        for i in arr:
            temp="{0:b}".format(i)
            curr=temp.count("1")
            if curr not in dic:
                dic[curr]=[i]
            else:
                dic[curr].append(i)
        hashtable=dict(sorted(dic.items()))
        for i in hashtable:
            result+=hashtable[i]
        return result
    
    
    
            
        