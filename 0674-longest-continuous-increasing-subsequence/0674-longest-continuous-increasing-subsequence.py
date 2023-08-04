class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                dp[i]+=dp[i+1]
            
        return max(dp)