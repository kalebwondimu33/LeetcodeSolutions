class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        first=nums[-1]-1
        second=nums[-2]-1
        return first*second
        
        