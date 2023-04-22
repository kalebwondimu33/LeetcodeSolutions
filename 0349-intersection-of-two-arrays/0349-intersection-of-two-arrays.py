class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        result=set()
        for i in nums1:
            if i not in dic:
                dic[i]=1
        for i in nums2:
            if i in dic:
                result.add(i)
        return result
        