class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i!=j:
                    if nums[j]<nums[i]:
                        count+=1
            arr[i]=count
        return arr
            
        
        