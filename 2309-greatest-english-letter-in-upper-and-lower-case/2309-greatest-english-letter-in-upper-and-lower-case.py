class Solution:
    def greatestLetter(self, s: str) -> str:
        dic={}
        for j in s:
            if ord(j) in dic:
                dic[ord(j)]+=1
            else:
                dic[ord(j)]=1
        num=sorted(s)
        for i in range(len(num)-1,-1,-1):
            if ord(num[i])-32 in dic:
                return num[i].upper()
        return ""
            
        