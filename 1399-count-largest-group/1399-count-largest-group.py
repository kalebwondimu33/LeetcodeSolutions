class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic={}
        count=0
        for i in range(1,n+1):
            if len(str(i))==1:
                dic[i]=1
            elif len(str(i))>1:
                temp=sum(map(int,str(i)))
                if temp in dic:
                    dic[temp]+=1
                else:
                    dic[temp]=1
        value=list(dic.values())
        lar=max(value)
        for i in value:
            if i==lar:
                count+=1
        return count
            
                
            
        