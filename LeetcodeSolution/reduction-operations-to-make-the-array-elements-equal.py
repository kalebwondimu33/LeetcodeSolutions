class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        temp=[0]*len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                temp[i]=temp[i-1]
            elif nums[i]!=nums[i-1]:
                temp[i]=temp[i-1]+1
        return sum(temp)


        