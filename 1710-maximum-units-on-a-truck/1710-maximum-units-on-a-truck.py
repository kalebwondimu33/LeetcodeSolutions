class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap=[(-unit,boxsize) for boxsize,unit in boxTypes]
        heapq.heapify(heap)
        max_unit=0
        while heap and truckSize:
            unit,boxsize=heapq.heappop(heap)
            if boxsize<=truckSize:
                max_unit+=(-unit*boxsize)
                truckSize-=boxsize
            else:
                max_unit+=(-unit*truckSize)
                truckSize=0
        return max_unit
                
                
            
        