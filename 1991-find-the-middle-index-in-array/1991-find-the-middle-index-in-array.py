class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum=0
        right_sum=0
        total=sum(nums)
        fixed=total
        for i,v in enumerate(nums):
            right_sum=total-v
            left_sum=fixed-total
            if right_sum==left_sum:
                return i
            total-=v
        return -1