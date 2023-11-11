class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashtable={}
        ans=[]
        for i in nums:
            if i not in hashtable:
                hashtable[i]=1
            else:
                ans.append(i)
        return ans
                
        