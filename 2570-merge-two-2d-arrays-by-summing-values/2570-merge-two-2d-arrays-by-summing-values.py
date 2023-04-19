class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashtable={}
        result=[]
        for i,j in nums1:
            if i in hashtable:
                hashtable[i]+=j
            else:
                hashtable[i]=j
        for i,j in nums2:
            if i in hashtable:
                hashtable[i]+=j
            else:
                hashtable[i]=j
        for k,v in hashtable.items():
            result.append([k,v])
        return sorted(result)
            
            
        