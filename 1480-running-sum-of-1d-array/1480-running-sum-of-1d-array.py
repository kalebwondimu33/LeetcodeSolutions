class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(1,len(nums)+1):
            result.append(sum(nums[:i]))
        return result