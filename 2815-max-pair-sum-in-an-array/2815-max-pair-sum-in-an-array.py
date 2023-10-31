class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxx=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if max(str(nums[i]))==max(str(nums[j])):
                    maxx=max(maxx,nums[i]+nums[j])
        return maxx
                
        
                                             
        