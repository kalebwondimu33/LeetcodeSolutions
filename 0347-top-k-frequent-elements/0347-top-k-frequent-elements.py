class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        count=[(-v,k)for k,v in count.items()]
        heapq.heapify(count)
        output=[]
        print(count)
        for i in range(k):
            item=heapq.heappop(count)
            print(item)
            output.append(item[1])
        return output
        
            
            