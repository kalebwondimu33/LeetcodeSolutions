class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_part(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    if mid==0:
                        return 0
                    elif nums[mid-1]==target:
                        right=mid-1
                    else:
                        return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        def right_part(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    if mid==len(nums)-1:
                        return mid
                    elif nums[mid+1]==target:
                        left=mid+1
                    else:
                        return mid
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        l=left_part(nums,target)
        r=right_part(nums,target)
        return [l,r]
            
            