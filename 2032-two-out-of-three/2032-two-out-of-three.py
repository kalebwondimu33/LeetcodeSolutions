class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
            elif i in nums3 and i not in result:
                result.append(i)
        for j in nums2:
            if j in nums3 and j not in result:
                result.append(j)
        return result
                
            
        