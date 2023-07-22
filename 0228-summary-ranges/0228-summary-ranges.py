class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start,curr,end=nums[0],nums[0],None
        ans=[]
        for i in nums[1:]:
            curr+=1
            if curr==i:
                end=i
            else:
                if not end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                start=i
                curr=i
                end=None
        if not end:
            ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return ans
        
                
        
                
        