class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                newvalue=nums[i-1]+1
                count+=newvalue-nums[i]
                nums[i]=newvalue
        return count
        