class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        repeat = 0
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                repeat += duration - diff
        return len(timeSeries)*duration - repeat