class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        countR=senate.count("R")
        countD=senate.count("D")
        banD=0
        banR=0
        qeue=deque(senate)
        while countR!=0 and countD!=0:
       
            if qeue[0]=="R":
                if banR>0:
                  banR-=1
                  countR-=1
                  qeue.popleft()
                else:
                    # countD-=1
                    banD+=1
                    temp=qeue.popleft()
                    qeue.append(temp)

            else:
                if banD>0:
                    banD-=1
                    countD-=1
                    qeue.popleft()
                else:
                    # countR-=1
                    banR+=1
                    temp=qeue.popleft()
                    qeue.append(temp)
  
        if countR>countD:
            return "Radiant"
        else:
            return "Dire"
        

        
                