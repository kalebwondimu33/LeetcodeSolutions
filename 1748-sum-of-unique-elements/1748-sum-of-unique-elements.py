class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashtable={}
        for i in nums:
            if i in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1
        total=0
        for i in nums:
            if hashtable[i]==1:
                total+=i
        return total
            
        