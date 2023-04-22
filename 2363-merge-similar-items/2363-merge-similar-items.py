class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashtable={}
        result=[]
        for i,j in items1:
            hashtable[i]=j
        for i,j in items2:
            if i in hashtable:
                hashtable[i]+=j
            else:
                hashtable[i]=j
        for v,w in hashtable.items():
            result.append([v,w])
        result.sort()
        return result
                
            
        
            
        