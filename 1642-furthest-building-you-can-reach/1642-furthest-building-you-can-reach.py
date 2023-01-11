class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N=len(heights)
        heap=[]
        for i  in range(N-1):
            diff=heights[i+1]-heights[i]
            if diff<=0:
                continue
            heapq.heappush(heap,diff)
            if len(heap)>ladders:
                min_h=heapq.heappop(heap)
                bricks-=min_h
            if bricks<0:
                return i
        return N-1
        
        