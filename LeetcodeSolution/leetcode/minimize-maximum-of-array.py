class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            total+=nums[i]
            ave=ceil(total/(i+1))
            res=max(res,ave)
        return res
            
                



        