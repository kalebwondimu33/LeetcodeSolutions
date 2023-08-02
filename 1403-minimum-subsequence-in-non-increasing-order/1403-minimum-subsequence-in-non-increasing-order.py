class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total=0
        left=0
        while left<len(nums):
            total=sum(nums[left+1:])
            
            if sum(nums[:left+1])>total:
                return nums[:left+1]
            else:
                left+=1
            