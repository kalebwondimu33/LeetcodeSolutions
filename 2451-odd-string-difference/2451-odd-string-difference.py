class Solution:
    def oddString(self, words: List[str]) -> str:
        k=len(words[0])
        arr=[]
        for i in words:
            l=[]
            for j in range(1,k):
                diff=ord(i[j])-ord(i[j-1])
                l.append(diff)
            arr.append(l)
        for i in range(len(arr)):
            if arr.count(arr[i])==1:
                return words[i]
            
            
        