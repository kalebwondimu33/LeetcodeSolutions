class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        n=len(nums)
        target=total%p
        if target==0:
            return 0
        rem=0
        dct={0:-1}
        for i,v in enumerate(nums):
            rem=(rem+v)%p
           
            if (rem-target)%p in dct:
               
                n=min(n,i-dct[(rem-target)%p])
            dct[rem]=i
        return -1 if n==len(nums) else n

        

