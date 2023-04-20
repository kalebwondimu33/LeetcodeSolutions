class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if Counter(target)==Counter(arr):
            return True
        else:
            return False
        