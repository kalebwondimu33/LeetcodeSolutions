class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref_sum=0
        ans=nums[0]
        for num in nums:
            if pref_sum<0:
                pref_sum=0
            pref_sum+=num
            ans=max(ans,pref_sum)
        return ans
            
        