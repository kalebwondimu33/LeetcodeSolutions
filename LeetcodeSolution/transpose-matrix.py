class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            transpose.append(temp)
        return transpose
                
                
        