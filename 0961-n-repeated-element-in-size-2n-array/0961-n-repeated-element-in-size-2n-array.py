class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashtable={}
        for i in nums:
            if i in hashtable:
                hashtable[i]+=1
            else:
                hashtable[i]=1
        for i in nums:
            if hashtable[i]>1:
                return i
        