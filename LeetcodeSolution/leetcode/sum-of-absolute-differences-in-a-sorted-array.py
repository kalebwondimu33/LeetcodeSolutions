class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref_sum=[]
        temp=0
        n=len(nums)
        ans=[]
        for i in range(len(nums)):
            temp+=nums[i]
            pref_sum.append(temp)
        total=pref_sum[-1]
        print(total)
        for j in range(len(nums)):
            if j==0:
                curr=(total-nums[j])-((n-j-1)*nums[j])
                ans.append(curr)
            elif j==n-1:
                ans.append((j*nums[j])-(total-nums[j]))
            else:
                ans.append((j*nums[j]-pref_sum[j-1])+((total-pref_sum[j])-((n-j-1)*nums[j])))
        
        return ans
        