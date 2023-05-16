class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        result=set()
        average=0
        while left<right:
            average=(nums[left]+nums[right])/2
            result.add(average)
            left+=1
            right-=1
        return len(result)
            
        