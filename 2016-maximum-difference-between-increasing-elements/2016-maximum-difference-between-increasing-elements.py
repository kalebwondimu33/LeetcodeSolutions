class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                max_diff=max(nums[j]-nums[i],max_diff)
        if max_diff>0:
            return max_diff
        else:
            return -1
            
        