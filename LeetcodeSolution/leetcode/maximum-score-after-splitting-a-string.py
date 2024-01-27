class Solution:
    def maxScore(self, s: str) -> int:
        if len(s)==2:
            if s=="10":
                return 0
            elif s in ["00","11"]:
                return 1
            else:
                return 2
        score=[]
        ctn=0
        for i in range(len(s)):
            if s[i]=="0":
                ctn+=1
            score.append(ctn)
        ctn=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                ctn+=1
            score[i]+=ctn
        return max(score[1:-1])
      
        
        
       
        
      
            
        