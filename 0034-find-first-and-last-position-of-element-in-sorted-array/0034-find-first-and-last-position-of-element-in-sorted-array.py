class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_extreme(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    if mid==0:
                        return 0
                    if nums[mid-1]==target:
                        r=mid-1
                    else:
                        return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        def right_extreme(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    if mid==len(nums)-1:
                        return mid
                    if nums[mid+1]==target:
                        l=mid+1
                    else:
                        return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        left=left_extreme(nums,target)
        right=right_extreme(nums,target)
        return [left,right]