class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        res=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=sum((nums[i],nums[l],nums[r]))
                if s==0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif s>0:
                    r-=1
                else:
                    l+=1
        for i in ans:
            res.append(list(i))
        return res
        