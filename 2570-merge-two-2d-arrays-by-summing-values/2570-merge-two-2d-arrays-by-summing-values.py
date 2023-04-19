class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashtable={}
        result=[]
        for i in nums1:
            for j in range(len(i)-1):
                hashtable[i[j]]=i[j+1]
        for i in nums2:
            for j in range(len(i)-1):
                if i[j] not in hashtable:
                    hashtable[i[j]]=i[j+1]
                else:
                    hashtable[i[j]]+=i[j+1]
                    
        for k,v in hashtable.items():
            result.append([k,v])
        return sorted(result)
            
            
        