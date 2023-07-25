class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count=Counter(nums)
        nums=sorted(list(set(nums)))
        earn1,earn2=0,0
        for i in range(len(nums)):
            cur_earn=nums[i]*count[nums[i]]
            if i>0 and nums[i]==nums[i-1]+1:
                temp=earn2
                earn2=max(cur_earn+earn1,earn2)
                earn1=temp
            else:
                temp=earn2
                earn2=cur_earn+earn2
                earn1=temp
        return earn2
        