class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        ans=[]
        count=Counter(nums)
        for i in count:
            if count[i]>n:
                ans.append(i)
        return ans
        
        