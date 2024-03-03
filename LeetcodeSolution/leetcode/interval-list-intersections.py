class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output=[]
        for x,y in firstList:
            for i,j in secondList:
               if i>=x and i<=y:
                   first=max(i,x)
                   second=min(j,y)
                   output.append([first,second])
               elif j>=x and j<=y:
                   first=max(i,x)
                   second=min(j,y)
                   output.append([first,second])
               elif x>=i and x<=j:
                   first=max(i,x)
                   second=min(j,y)
                   output.append([first,second])
               elif y>=j and y<=i:
                   first=max(i,x)
                   second=min(j,y)
                   output.append([first,second])



        return output

        