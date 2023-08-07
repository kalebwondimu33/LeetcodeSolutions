class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dic=Counter(n%2 for n in position)
        return min(dic[0],dic[1])
        