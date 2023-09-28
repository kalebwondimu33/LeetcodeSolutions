class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result=[]
        for x,y in nums:
            for i in range(x,y+1):
                if i not in result:
                    result.append(i)
        return len(result)
        