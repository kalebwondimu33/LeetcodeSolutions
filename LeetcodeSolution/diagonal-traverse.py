class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        dic={}
        ans=[]
        for i in range(n):
            for j in range(m):
                temp=i+j
                if temp not in dic:
                    dic[temp]=[mat[i][j]]
                else:
                    dic[temp].append(mat[i][j])
        for k in dic:
            if k%2==0:
                ans.extend(dic[k][::-1])
            else:
                ans.extend(dic[k])
        print(dic)
        print(ans)
        return ans