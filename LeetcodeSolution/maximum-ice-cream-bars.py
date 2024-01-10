class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxx=0
        count=0
        costs.sort()
        for r in range(len(costs)):
            maxx+=costs[r]
            if maxx<coins:
                count+=1
            elif maxx==coins:
                count+=1
                break
            else:
                break
        return count
