class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        special=0
        n=len(nums)
        for i in range(len(nums)):
            j=i+1
            if n%j==0:
                special+=nums[i]**2
        return special
        