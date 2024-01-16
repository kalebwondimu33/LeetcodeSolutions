class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp=0
        for i,v in enumerate(nums):
            temp+=v
            nums[i]=temp
        return nums