class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result=[0]*len(nums)
        res=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                result[i]=1+result[i-1]
                res+=result[i]
        return res
            
                
             