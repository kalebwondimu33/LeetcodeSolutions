class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=int)
        for i in range(1,len(nums)+1):
            if i==k:
                return nums[-i]
            