class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            left_sum=sum(nums[:i])
            right_sum=sum(nums[i:])-nums[i]
            result.append(abs(left_sum-right_sum))
        return result
        