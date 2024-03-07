class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        best=float("inf")
        while left<=right:
            mid=(left+right)//2
            total=0
            for num in nums:
                total+=ceil(num/mid)
            if total>threshold:
                left=mid+1
            else:
                best=mid
                right=mid-1
        return best
        