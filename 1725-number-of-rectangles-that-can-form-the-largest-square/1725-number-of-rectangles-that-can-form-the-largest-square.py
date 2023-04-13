class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        result=[]
        for i in rectangles:
                count=min(i[0],i[1])
                result.append(count)
        return result.count(max(result))
            
        