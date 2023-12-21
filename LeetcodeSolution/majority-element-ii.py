class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        rep=len(nums)/3
        ans=[]
        for i in count:
            if count[i]>rep:
                ans.append(i)
        return ans
        