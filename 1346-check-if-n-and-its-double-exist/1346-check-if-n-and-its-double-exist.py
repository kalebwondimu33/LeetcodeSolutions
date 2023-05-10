class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]*2 in arr and i!=arr.index(arr[i]*2):
                return True
        return False
        