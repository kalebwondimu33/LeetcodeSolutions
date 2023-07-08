class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        nums.sort()
        left=0
        right=len(nums)
        mid=(left+right)//2
        return nums[mid]
        