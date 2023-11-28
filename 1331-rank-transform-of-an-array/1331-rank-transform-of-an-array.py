class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num=sorted(list(set(arr)))
        d={}
        start=1
        result=[0]*len(arr)
        for i in range(len(num)):
            if i==0:
                d[num[i]]=start
                start+=1
            elif num[i] in d:
                start+=1
                continue
            else:
                d[num[i]]=start
                start+=1
        for i in range(len(arr)):
            result[i]=d[arr[i]]
        return result
            
        
        