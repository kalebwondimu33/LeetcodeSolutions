class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_pair=0
        nums.sort()
        left=0
        right=len(nums)-1
        while left<=right:
            max_pair=max(max_pair,nums[left]+nums[right])
            left+=1
            right-=1
        return max_pair
        