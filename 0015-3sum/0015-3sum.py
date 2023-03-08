class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,v in enumerate(nums):
            if i>0 and v==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                three_sum=v+nums[l]+nums[r]
                if three_sum>0:
                    r-=1
                elif three_sum<0:
                    l+=1
                else:
                    res.append([v,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
                
        
            
        