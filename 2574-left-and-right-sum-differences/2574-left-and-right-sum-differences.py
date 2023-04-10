class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        fixed_total=sum(nums)
        for i,v in enumerate(nums):
            left_sum=fixed_total-total
            right_sum=total-v
            total-=v
            nums[i]=abs(left_sum-right_sum)
        return nums
            
        