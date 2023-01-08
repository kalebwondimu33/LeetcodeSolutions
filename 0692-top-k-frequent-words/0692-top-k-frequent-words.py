class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        count=[(-v,k)for k,v in count.items()]
        heapq.heapify(count)
        result=[]
        for i in range(k):
            items=heapq.heappop(count)
            result.append(items[1])
        return result
        