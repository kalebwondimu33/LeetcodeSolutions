class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        result=[]
        for i in rectangles:
            for j in range(1):
                count=min(i[0],i[1])
                result.append(count)
        return result.count(max(result))
            
        