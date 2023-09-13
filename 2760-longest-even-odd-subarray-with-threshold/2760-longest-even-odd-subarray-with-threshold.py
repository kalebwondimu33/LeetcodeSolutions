class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans=0
        for i in range(len(nums)):
            count=0
            if (nums[i]%2==0) and (nums[i]<=threshold):
                count=1
                for j in range(i+1,len(nums)):
                    if (nums[j]%2 == nums[j-1]%2) or nums[j]>threshold:
                        break
                    count+=1
            ans=max(ans,count)
        return ans
            
        
        
       