class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans=0
        l=list(zip(*strs))
        for item in l:
            for i in range(1,len(item)):
                if item[i]<item[i-1]:
                    ans+=1
                    break
        return ans
  

                
        