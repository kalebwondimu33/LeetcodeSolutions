class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if -target <= nums[i] - nums[j] <= target:
                    if dp[j] > -1:
                        dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]
                
            
        