class Solution:
    def maxwin(self,nums,left,right,n):
        if left==right:
            return nums[left]
        left_sum=nums[left]-self.maxwin(nums,left+1,right,n)
        right_sum=nums[right]-self.maxwin(nums,left,right-1,n)
        return max(left_sum,right_sum)


    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        return self.maxwin(nums,0,n-1,n) >= 0


        
        