class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        result=[]
        nums.sort()
        left=0
        right=len(nums)-1
        while left<=right:
            sum=nums[left]+nums[right]
            result.append(sum)
            left+=1
            right-=1
        return max(result)
        