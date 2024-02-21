class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        mid=len(costs)//2
        costs.sort(key=lambda x : x[0]-x[1])
        ans=0
        for i in range(mid):
            ans+=costs[i][0]+costs[mid+i][1]
        return ans



