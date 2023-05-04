class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total=0
        gre=max(nums)
        for i in range(k):
            total+=gre
            gre+=1
        return total
            
        