class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_attitude=0
        count=0
        for i in gain:
            count=count+i
            max_attitude=max(max_attitude,count)
        return max_attitude