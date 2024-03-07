class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod=10**9 + 7
        count=defaultdict(int)
        for num in nums:
            temp=num-int(str(num)[::-1])
            count[temp]+=1
        ans=0
        for c in count:
            n=count[c]-1
            ans+=((n/2)*(n+1))
        return int(ans)%mod
        