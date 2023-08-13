class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_list=[]
        for x in arr2:
            while x in arr1:
                sorted_list.append(x)
                arr1.remove(x)
        return sorted_list+sorted(arr1)
        

        