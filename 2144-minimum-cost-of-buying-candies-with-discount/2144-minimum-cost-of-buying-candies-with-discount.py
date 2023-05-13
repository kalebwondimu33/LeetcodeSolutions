class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        if len(cost)<=2:
            return sum(cost)
        total=0
        while cost:
            total+=cost.pop()
            if cost:
                total+=cost.pop()
            if cost:
                cost.pop()
        return total
            
        
        