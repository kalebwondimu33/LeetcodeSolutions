class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref=[0]*(len(nums)+1)
        nums.sort()
        for s,e in requests:
            pref[s]+=1
            pref[e+1]-=1
        for i in range(1,len(pref)):
            pref[i]+=pref[i-1]
        pref.sort(reverse=True)
        ans=0
        for num in pref:
            if num!=0:
                ans+=(num*nums.pop())
            else:
                return ans%(10**9+7)

        return ans%(10**9+7)
        

        
        