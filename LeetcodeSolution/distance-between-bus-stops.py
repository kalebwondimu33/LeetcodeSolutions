class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total=sum(distance)
        if start<destination:
            clock=sum(distance[start:destination])
            counter_clock=total-clock
            
        else:
            counter_clock=sum(distance[destination:start])
            clock=total-counter_clock
        return min(clock,counter_clock)
            
            
            
        
        