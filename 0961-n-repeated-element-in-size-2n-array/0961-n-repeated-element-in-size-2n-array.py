class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hashtable={}
        for i in nums:
            if i in hashtable:
                return i
            hashtable[i]=1
        