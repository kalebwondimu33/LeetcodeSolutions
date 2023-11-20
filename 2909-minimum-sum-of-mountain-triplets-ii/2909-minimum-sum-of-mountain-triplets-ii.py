class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_l=[nums[0]]*len(nums)
        min_r=[nums[-1]]*len(nums)
        for i in range(1,len(nums)):
            min_l[i]=min(nums[i],min_l[i-1])
        for j in range(len(nums)-2,-1,-1):
            min_r[j]=min(nums[j],min_r[j+1])
        ans=float("inf")
        for k in range(1,len(nums)-1):
            if min_l[k]<nums[k] and min_r[k]<nums[k]:
                ans=min(ans,nums[k]+min_l[k]+min_r[k])
        if ans==float("inf"):
            return -1
        else:
            return ans
            
        
        
        