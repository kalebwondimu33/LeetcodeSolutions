class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=sorted(nums)
        d={}
        result=[0]*len(nums)
        start=0
        for i in range(len(arr)):
            if i==0:
                d[arr[i]]=0
                start+=1
            elif arr[i] in d:
                start+=1
                continue
            else:
                d[arr[i]]=start
                start+=1
        for i in range(len(nums)):
            result[i]=d[nums[i]]
        return result
        
            
        
        