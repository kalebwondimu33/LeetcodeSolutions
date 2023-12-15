class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total1=sum(nums)
        n=len(nums)
        alltotal=sum([i for i in range(n+1)])
        print(alltotal)
        return alltotal-total1