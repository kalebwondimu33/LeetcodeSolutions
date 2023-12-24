class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d_winner={}
        d_loser={}
        ans=[]
        for x,y in matches:
            if x in d_winner:
                d_winner[x]+=1
            if x not in d_winner:
                d_winner[x]=1
            if y in d_loser:
                d_loser[y]+=1
            if y not in d_loser:
                d_loser[y]=1
        win=[]
        lose=[]
        for k in d_winner:
            if k not in d_loser:
                win.append(k)
        for j in d_loser:
            if d_loser[j]==1:
                lose.append(j)
        win.sort()
        lose.sort()
        ans.append(win)
        ans.append(lose)
        return ans
            
        