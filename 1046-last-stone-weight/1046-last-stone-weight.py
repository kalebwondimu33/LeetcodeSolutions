class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone_one=-(heapq.heappop(stones))
            stone_two=-(heapq.heappop(stones))
            left_over=abs(stone_one-stone_two)
            heapq.heappush(stones,-left_over)
        return -stones[0]
        