class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        temp=sorted(nums)
        result=[]
        for i in range(len(temp)):
            if temp[i]==target:
                result.append(i)
        return result