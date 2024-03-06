# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        minn=float("inf")
        while left<=right:
            mid=(left+right)//2
            ans=isBadVersion(mid)
            if not ans:
                left=mid+1
            else:
                minn=min(minn,mid)
                right=mid-1
        
        return minn
            
        
        