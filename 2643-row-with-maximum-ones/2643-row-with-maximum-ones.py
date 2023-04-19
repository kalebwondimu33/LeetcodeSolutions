class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        result=[]
        hashtable={}
        for i,v in enumerate(mat):
            count=0
            for j in range(len(v)):
                if v[j]==1:
                    count+=1
            hashtable[i]=count
        index=0
        max_one=0
        for i in hashtable:
            if hashtable[i]>max_one:
                max_one=hashtable[i]
                index=i
        result.append(index)
        result.append(max_one)
        return result
            
        