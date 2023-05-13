class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        postive=heapq.nlargest(3,nums)
        negative=heapq.nsmallest(2,nums)
        return max(negative[0]*negative[1]*postive[0],postive[0]*postive[1]*postive[2])
            
        