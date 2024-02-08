class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic={0:1}
        total=0
        ans=0
        for i in nums:
            total+=i
            diff=total-goal
            if diff in dic:
                ans+=dic[diff]
            dic[total]=1+dic.get(total,0)
        return ans
