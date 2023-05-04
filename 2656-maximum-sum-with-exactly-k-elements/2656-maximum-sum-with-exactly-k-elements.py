class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total=0
        nums.sort()
        for i in range(k):
            total+=nums[-1]
            nums[-1]=nums[-1]+1
        return total
            
        