class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            result.append(len(set(nums[:i+1]))-len(set(nums[i+1:])))
        return result
            
        