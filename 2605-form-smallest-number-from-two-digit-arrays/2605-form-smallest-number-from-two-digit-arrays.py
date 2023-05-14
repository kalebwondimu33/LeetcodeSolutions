class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nset=set(nums1)&set(nums2)
        if nset:
            return min(nset)
        else:
            first=min(nums1)
            second=min(nums2)
            if first>second:
                return int(str(second)+str(first))
            else:
                return int(str(first)+str(second))
                
        