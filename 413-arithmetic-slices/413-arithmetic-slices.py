class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)>2:
            diff=nums[1]-nums[0]
            count=2
            total_sum=0
            for i in range(1,len(nums)-1):
                current_diff=nums[i+1]-nums[i]
                if current_diff==diff:
                    count+=1
                else:
                    total_sum+=((count-1)*(count-2))//2
                    count=2
                    diff=current_diff
            return total_sum+((count-1)*(count-2))//2
        else:
            return 0
      
                
           
        