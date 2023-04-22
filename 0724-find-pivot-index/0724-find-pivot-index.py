class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=sum(nums)
        for i,v in enumerate(nums):
            if left_sum==right_sum-v-left_sum:
                return i
            left_sum+=v
        return -1
            
        