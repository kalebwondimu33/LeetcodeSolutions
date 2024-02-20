class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count=0
        i=0
        while tickets[k]!=0:
            if tickets[i]!=0:
                count+=1
                tickets[i]-=1
            i=(i+1)%len(tickets)
        return count
            
        