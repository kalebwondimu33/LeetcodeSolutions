class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        count=Counter(nums1)
        nums2.sort()
        for i in nums2:
            if i in count:
                return i
        first=min(nums1)
        second=min(nums2)
        if first>second:
            return int(str(second)+str(first))
        else:
            return int(str(first)+str(second))
                
        