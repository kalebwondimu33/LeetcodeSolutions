class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        one=0
        zero=0
        d={}
        result=[]
        for i in nums:
            one+=i
        for j in range(len(nums)):
            if j==0:
                ans[j]=one
                if nums[j]==1:
                    one-=1
                else:
                    zero+=1
            else:
                ans[j]=zero+one
                if nums[j]==0:
                    zero+=1
                else:
                    one-=1
        ans.append(zero)  
        for j in range(len(ans)):
            d[j]=ans[j]
        maxx=max(d.values())
        for k in d:
            if d[k]==maxx:
                result.append(k)

        return result
        
            
            
            
        
        