class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        station=arrivalTime+delayedTime
        if station>=24:
            return station%24
        else:
            return station
        