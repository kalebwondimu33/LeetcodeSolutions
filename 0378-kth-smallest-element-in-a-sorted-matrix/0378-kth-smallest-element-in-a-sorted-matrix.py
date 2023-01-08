class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result=[]
        for i in matrix:
            for j in range(len(i)):
                result.append(i[j])
        result.sort()
        return result[k-1]
                
        