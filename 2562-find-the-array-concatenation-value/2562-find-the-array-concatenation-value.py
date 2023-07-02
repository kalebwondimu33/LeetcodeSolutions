class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        con_value=0
        left=0
        right=len(nums)-1
        if len(nums)%2==0:
            while left<right:
                add=str(nums[left])+str(nums[right])
                con_value+=int(add)
                left+=1
                right-=1
        else:
            while left<=right:
                if left==right:
                    add=str(nums[left])
                    con_value+=int(add)
                    left+=1
                    right-=1
                else:
                    add=str(nums[left])+str(nums[right])
                    con_value+=int(add)
                    left+=1
                    right-=1
        return con_value
        