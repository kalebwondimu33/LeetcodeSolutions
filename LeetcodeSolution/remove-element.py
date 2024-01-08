class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seek=0
        pos=0
        while seek<len(nums):
            if nums[seek]!=val:
                nums[pos],nums[seek]=nums[seek],nums[pos]
                pos+=1
            seek+=1
        return pos


        

        