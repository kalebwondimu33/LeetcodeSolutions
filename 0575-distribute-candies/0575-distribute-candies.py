class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dic={}
        temp=len(candyType)//2
        for i in candyType:
            if i  in dic:
                dic[i]+=1
            else:
                dic[i]=1
        if len(dic)>temp:
            return temp
        else:
            return len(dic)
        