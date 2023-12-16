class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_ans=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])<=min(nums[i],nums[j]):
                    max_ans=max(max_ans,nums[i]^nums[j])
        return max_ans
        