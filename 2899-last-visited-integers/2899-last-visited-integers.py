class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        k,li,ans=0,[],[]
        for  i in words:
            if i=="prev":
                k+=1
                if k>len(li):
                    ans.append(-1)
                else:
                    ans.append(li[-k])
            else:
                k=0
                li.append(int(i))
        return ans
    
     
        