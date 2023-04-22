class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique_num1=[]
        unique_num2=[]
        for i in nums1:
            if i not in nums2 and i not in unique_num1:
                unique_num1.append(i)
        for i in nums2:
            if i not in nums1 and i not in unique_num2:
                unique_num2.append(i)
        return [unique_num1,unique_num2]
        